from typing import Any, TypeVar

T = TypeVar("T")


def get_last_item(ls: list[Any]) -> Any:
    "if empty list, return None"
    try:
        return ls[-1]
    except IndexError:
        return None


def extract_last_two_items(ls: list[Any]) -> list[Any]:
    "put them in a list. If ls is less than two items, it should return it as it is"
    return ls[-2:]


def add_first_with_last(ls: list[int]) -> int | None:
    "if ls has one element, return it. If ls is empty, return None"
    if len(ls) == 1:
        return ls[0]
    if ls == []:
        return None
    return ls[0] + ls[-1]
    # # Another solution:
    # match ls:
    #     case [x, *_, y]:
    #         return x + y
    #     case [x]:
    #         return x
    #     case []:
    #         return None


def combine_last_letters(text1: str, text2: str) -> str:
    """
    Example:
        text1: "Ahmed"
        text2: "Salem"
        Answer: "dm"
    if one text is empty (i.e., ""), return the last letter of the other
    if both are empty, return empty
    """
    if text1 and not text2:
        return text1[-1]
    if text2 and not text1:
        return text2[-1]
    if not text1 and not text2:
        return ""
    return text1[-1] + text2[-1]
    # Another solution
    # t1 = list(text1)
    # t2 = list(text2)

    # match (t1, t2):
    #     case ([*_, last1], [*_, last2]):
    #         return last1 + last2
    #     case ([], [*_, last]) | ([*_, last], []):
    #         return last
    #     case _:
    #         return ""


def add_even_number(num: int, ls: list[int]) -> list[int]:
    "add the number to the list only if it's even and return the list"
    new_list = ls.copy()
    if num % 2 != 0:
        return new_list
    new_list.append(num)
    return new_list


def swap_last_with_first(ls: list[T]) -> list[T]:
    "[1, 2, 3] -> [3, 2, 1]. If ls has less than 2 elements, return ls as it is"
    match ls:
        case [first, *middle, last]:
            return [last, *middle, first]
        case _:
            return ls
