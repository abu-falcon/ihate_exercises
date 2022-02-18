import random
from ast import arguments
from pathlib import Path

import pytest
from ihat_exercises.exercise_2 import (
    calculate_upper_lower,
    find_files_starts_with,
    multiply_numbers,
    unique_numbers,
)


@pytest.fixture
def folder_pretext(tmp_path):
    def another_func(pre_text, times, fake_text):
        for _ in range(times):
            file = (
                tmp_path
                / f"{pre_text}_{random.randint(0, 1000)}_{random.choice(['A', 'B', 'C'])}{random.choice(['A', 'B', 'C'])}"
            )
            file.touch()
        for i in range(times):
            file = tmp_path / f"{fake_text}{i}"
            file.touch()
        return str(tmp_path)

    return another_func


@pytest.mark.parametrize(
    "iterable, expected", [([1, 2], 2), ((0,), 0), ({1: 1, 3: 3, 2: 2}, 6), ([], 1)]
)
def test_multiply_numbers(iterable, expected) -> None:
    assert multiply_numbers(iterable) == expected


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("I Love Pasta", (3, 7)),
        ("ABOOD HAMOOD", (11, 0)),
        ("    ", (0, 0)),
        ("111", (0, 0)),
        ("abc", (0, 3)),
    ],
)
def test_calculate_upper_lower(sentence, expected):
    assert calculate_upper_lower(sentence) == expected


@pytest.mark.parametrize(
    "iterable, expected",
    [
        ([1, 1, 2], [1, 2]),
        ((2, 1, 2), [2, 1]),
        ([], []),
        ([0], [0]),
        ({1: 1, 1: 2, 3: 3, 1: 3}, [1, 3]),
    ],
)
def test_unique_numbers(iterable, expected):
    assert unique_numbers(iterable) == expected


@pytest.mark.parametrize(
    "pretext, times, fake_text",
    [
        ("hello", 10, "hi"),
        ("hi", 3, "hi"),
        ("ku", 5, "kuu"),
        ("yes", 5, "ye"),
    ],
)
def test_find_files_starts_with(folder_pretext, pretext, times, fake_text):
    folder = folder_pretext(pretext, times, fake_text)
    if pretext in fake_text:
        assert len(find_files_starts_with(pretext, folder)) == (2 * times)
        return
    assert len(find_files_starts_with(pretext, folder)) == times
