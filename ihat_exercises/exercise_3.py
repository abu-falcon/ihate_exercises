from typing import Any, TypeVar

T = TypeVar("T")


def get_last_item(ls: list[Any]) -> Any:
    "if empty list, return None. It will pass one of the tests if not implemented"


def extract_last_two_items(ls: list[Any]) -> list[Any]:
    "put them in a list. If ls is less than two items, it should return it as it is"


def add_first_with_last(ls: list[int]) -> int | None:
    "if ls has one element, return it. If ls is empty, return None. It will pass one of the tests if not implemented"


def combine_last_letters(text1: str, text2: str) -> str:
    """
    Example:
        text1: "Ahmed"
        text2: "Salem"
        Answer: "dm"
    if one text is empty (i.e., ""), return the last letter of the other
    if both are empty, return empty
    """


def add_even_number(num: int, ls: list[int]) -> list[int]:
    "add the number to the list only if it's even and return the list"


def swap_last_with_first(ls: list[T]) -> list[T]:
    "[1, 2, 3] -> [3, 2, 1]. If ls has less than 2 elements, return ls as it is"
