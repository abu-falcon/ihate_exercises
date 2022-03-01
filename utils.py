import asyncio
import inspect
import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Awaitable, Callable, TypeVar

R = TypeVar("R")


async def run_command(cmd: str) -> list[str]:
    "run any OS command. For example 'ls -a'. The return will be the result of the command cut by new line character"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    result, _ = await process.communicate()
    return result.decode().splitlines()


async def run_xgen(job: Path, xgen: str) -> None:
    dir_, rest = make_dirs(job.with_suffix(""))
    move(job, dir_)
    out_name = job.with_suffix(".out").name
    process = await asyncio.create_subprocess_shell(
        f"{xgen} <{dir_/job.name} >{dir_/out_name}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    await process.communicate()
    move(dir_ / out_name, job.parant)
    move_rest(rest, job.parent / "rest")
    remove_dir(dir_)
    print(f"""{job.with_suffix(".out")} {xgen.upper()} is done""")


async def run_parallel_xgen(jobs: list[str], xgens: list[str]) -> None:
    awaitables = [run_xgen(job, xgen) for job, xgen in zip(jobs, xgens)]
    await run_parallel(*awaitables)


async def run_sequence_xgen(jobs: list[str], xgens: list[str]) -> None:
    awaitables = [run_xgen(job, xgen) for job, xgen in zip(jobs, xgens)]
    await run_sequence(*awaitables)


def make_dirs(folder: Path, rest_folder: bool = True) -> tuple[Path, Path]:
    folder.mkdir(exist_ok=True)
    if rest_folder:
        rest = folder / "rest"
        rest.mkdir(exist_ok=True)
    return folder, rest


def move(file: Path, destination: Path) -> None:
    shutil.copy(file, destination)


def move_rest(rest_folder: Path, destination: Path):
    for file in rest_folder.iterdir():
        shutil.copy(file, destination)


def remove_dir(dir_name: Path) -> None:
    shutil.rmtree(dir_name)


async def run_parallel(
    *args: Awaitable[R]
    | tuple[Callable[..., Awaitable[R]], list[Any]]
    | tuple[Callable[..., R], list[Any]]
) -> list[R]:
    awaitables = []
    exec = ThreadPoolExecutor()
    for arg in args:
        match arg:
            case (func, arguments) if inspect.iscoroutinefunction(func):
                awaitables.append(func(*arguments))
            case (func, arguments):
                loop = asyncio.get_running_loop()
                awaitables.append(loop.run_in_executor(exec, func, *arguments))
            case _:
                awaitables.append(arg)
    results = await asyncio.gather(*awaitables)
    exec.shutdown()
    return list(results)


async def run_sequence(
    *args: Awaitable[R]
    | tuple[Callable[..., Awaitable[R]], list[Any]]
    | tuple[Callable[..., R], list[Any]]
) -> list[R]:
    results = []
    loop = asyncio.get_running_loop()
    exec = ThreadPoolExecutor()
    for arg in args:
        match arg:
            case (func, arguments) if inspect.iscoroutinefunction(func):
                try:
                    result = await func(*arguments)
                except TypeError:
                    result = await func(result, *arguments)
                results.append(result)
            case (func, arguments):
                try:
                    result = await loop.run_in_executor(exec, func, *arguments)
                except TypeError:
                    result = await loop.run_in_executor(exec, func, result, *arguments)
                results.append(result)
            case _:
                result = await arg
                results.append(result)
    exec.shutdown()
    return results
