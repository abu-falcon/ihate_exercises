import re
import string
from typing import Iterable, TypeVar

T = TypeVar("T")
U = TypeVar("U")

ALL_LETTERS = string.ascii_letters


def extract_SIG_letters(d: dict[str, str]) -> list[tuple[str, str]]:
    """
    extract value and key if the key matches exactly 'SIG' + (one or more letter [small/big]) + (anything else [could be empty])

    Example:

    {
        "heSIGabc": "a",
        "sigabc": "b",
        "SIGABc": "c",
        "SIGab3": "d",
        "SIBabc": "e",
        "SIGa": "f",
        "SIG": "g",
        "SIGk11111A": "h",

    }    ---> [("c", "SIGABc"), ('d', 'SIGab3'), ("f", "SIGa"), ("h","SIGk11111A")]
    """


def combine_two_lists(iter1: Iterable[T], iter2: Iterable[U]) -> list[tuple[T, U]]:
    """
    Example:
        ls1 = [1, 2, 3]
        ls2 = [4, 5, 6]
        answer = [(1, 4), (2, 5), (3, 6)]
    If one list is smaller than the other, finish at the smaller one length
    """


def get_element_and_index(iter: Iterable[T]) -> list[tuple[int, T]]:
    """
    Example:
        iter = ("apple", "banana", "mango")
        answer = [(0, "apple"), (1, "banana"), (2, "mango")]
    """


def connect_strings_with_seperator(strings: Iterable[str], sep: str = " ") -> str:
    """
    Example:
        strings = ["I", "love", "Coca-Cola"]
        sep     = " "
        answer  = "I love Coca-Cola"
    """


def count_nonempty_lines_file(file: str) -> int:
    "open the file and extract all lines. Then check the number of nonempty lines"
