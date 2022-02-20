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
    result: list[tuple[str, str]] = []
    for k, v in d.items():
        key_cut = list(k)
        match key_cut:
            case ["S", "I", "G", let, *_] if let in ALL_LETTERS:
                result.append((v, k))
    return result
    ## Another solution
    # return [(v, k) for k, v in d.items() if re.match(r"SIG[a-zA-Z]+", k)]


def combine_two_lists(iter1: Iterable[T], iter2: Iterable[U]) -> list[tuple[T, U]]:
    """
    Example:
        ls1 = [1, 2, 3]
        ls2 = [4, 5, 6]
        answer = [(1, 4), (2, 5), (3, 6)]
    If one list is smaller than the other, finish at the smaller one length
    """
    result = []
    for pair in zip(iter1, iter2):
        result.append(pair)
    return result
    ## another solution
    # result = []
    # iter1 = list(iter1)
    # iter2 = list(iter2)
    # length1 = len(iter1)
    # length2 = len(iter2)
    # min_length = min(length1, length2)
    # for i in range(min_length):
    #     result.append((iter1[i], iter2[i]))
    # return result


def get_element_and_index(iter: Iterable[T]) -> list[tuple[int, T]]:
    """
    Example:
        iter = ("apple", "banana", "mango")
        answer = [(0, "apple"), (1, "banana"), (2, "mango")]
    """
    result = []
    for i, element in enumerate(iter):
        result.append((i, element))
    return result
    ## Another solution
    # result = []
    # ls = list(iter)
    # size = len(ls)
    # for i in range(size):
    #     pair = (i, ls[i])
    #     result.append(pair)
    # return result


def connect_strings_with_seperator(strings: Iterable[str], sep: str = " ") -> str:
    """
    Example:
        strings = ["I", "love", "Coca-Cola"]
        sep     = " "
        answer  = "I love Coca-Cola"
    """
    return sep.join(strings)

    ## Another solution
    # answer = ""
    # seq = list(strings)
    # last_element_index = len(seq) - 1
    # for i, word in enumerate(seq):
    #     answer += word
    #     if i == last_element_index:  # last word
    #         break
    #     answer += sep
    # return answer


def count_nonempty_lines_file(file: str) -> int:
    with open(file, "r") as f:
        text = f.read()
        lines = text.splitlines()
    count = 0
    for line in lines:
        if line.strip() == "":  # empty line
            continue
        count += 1
    return count
