from typing import Any, TypeVar

T = TypeVar("T")


def repeat_word(word: str) -> str:
    "space between them. If empty, the answer should be empty"
    if not word:
        return word
    return word + " " + word


def make_list(arg1: int, arg2: int, arg3: int) -> list[int]:
    return [arg1, arg2, arg3]


def make_tuple(arg1: int, arg2: int, arg3: int) -> tuple[int, int, int]:
    return (arg1, arg2, arg3)


def make_dictionary(name: str, age: int, car: str) -> dict[str, str | int]:
    return {"name": name, "age": age, "car": car}


def find_number_in_list(number: int, mylist: list[int]) -> bool:
    return number in mylist


def find_value_of_key(key: int | str, d: dict[int | str, T]) -> T | None:
    "If it can't find it, it should return None"
    return d.get(key)
