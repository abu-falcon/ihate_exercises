from pathlib import Path
from typing import Iterable


def multiply_numbers(numbers: Iterable[int]) -> int:
    "multiply all the numbers in a list"


def calculate_upper_lower(sentence: str) -> tuple[int, int]:
    """
    calculate the number of upper case letters and lower case letters
    use :method str.isupper: and  :method str.islower:
    """


def unique_numbers(numbers: Iterable[int]) -> list[int]:
    "make a sequence unique"


def find_files_starts_with(text: str, directory: str) -> set[str]:
    """
    iterate over a directory and find the files that start with a specific text.
    Example:
        text = "pre"
        directory has the following files:
            hello.job
            pre_file.inp
            jacket.txt
            hello_pre.txt
            previous.out
        the answer: {"pre_file.inp", "previous.out"}
    Hint:
        - Path(directory).iterdir() gives you an iterable[file]. Looping over it gives you the files
        - each file object has :attribute str name:
        - use :method str.startswith: to check if the file starts with the text
    """
