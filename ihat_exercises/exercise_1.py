from typing import Any, TypeVar

T = TypeVar("T")


def do_basic_math(num1: int, num2: int) -> int:
    "subtract num2 from num1 and return it as absolute"


def check_both_even(num1: int, num2: int) -> bool:
    "even means num modulus 2 = 0"


def check_negative(num: int) -> bool:
    """"""


def repeat_word(word: str) -> str:
    "space between them. If empty, the answer should be empty"


def make_list(arg1: int, arg2: int, arg3: int) -> list[int]:
    """"""


def make_tuple(arg1: int, arg2: int, arg3: int) -> tuple[int, int, int]:
    """"""


def make_single_element_tuple(element: T) -> tuple[T]:
    """"""


def make_dictionary(name: str, age: int, car: str) -> dict[str, str | int]:
    """"""


def find_number_in_list(number: int, mylist: list[int]) -> bool:
    """"""


def find_value_of_key(key: int | str, d: dict[int | str, T]) -> T | None:
    "If it can't find it, it should return None. It will pass one of the tests if not implemented."
