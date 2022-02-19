import pytest
from ihat_exercises.exercise_3 import (
    add_even_number,
    add_first_with_last,
    combine_last_letters,
    extract_last_two_items,
    get_last_item,
)


@pytest.mark.parametrize("ls, expected", [(["hi"], "hi"), ([1, 2, 3], 3), ([], None)])
def test_get_last_item(ls, expected):
    assert get_last_item(ls) == expected


@pytest.mark.parametrize(
    "ls, expected",
    [
        ([1, 2, 3, 4], [3, 4]),
        (["hello", "world"], ["hello", "world"]),
        ([], []),
        ([1], [1]),
    ],
)
def test_extract_last_two_items(ls, expected):
    assert extract_last_two_items(ls) == expected


@pytest.mark.parametrize(
    "ls, expected",
    [
        ([1, 3], 4),
        ([5], 5),
        ([], None),
        ([1, 2, 3, 4, 5], 6),
    ],
)
def test_add_first_with_last(ls, expected):
    assert add_first_with_last(ls) == expected


@pytest.mark.parametrize(
    "text1, text2, expected",
    [
        ("Ahmed", "Salem", "dm"),
        ("D", "U", "DU"),
        ("", "Hello7", "7"),
        ("You", "", "u"),
        ("", "", ""),
    ],
)
def test_combine_last_letters(text1, text2, expected):
    assert combine_last_letters(text1, text2) == expected


@pytest.mark.parametrize(
    "num, ls, expected",
    [(3, [], []), (4, [], [4]), (-4, [1, 2], [1, 2, -4]), (33, [7], [7])],
)
def test_add_number(num, ls, expected):
    assert add_even_number(num, ls) == expected
