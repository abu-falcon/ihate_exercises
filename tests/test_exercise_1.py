import pytest
from ihat_exercises.exercise_1 import (
    find_number_in_list,
    find_value_of_key,
    make_dictionary,
    make_list,
    make_tuple,
    repeat_word,
)


@pytest.fixture()
def sample_dict():
    sample_dict = {1: "one", "one": 1, "ls": [5, 7, 9]}
    return sample_dict


@pytest.mark.parametrize(
    "word, expected", [("Water", "Water Water"), ("Yes", "Yes Yes"), ("", "")]
)
def test_repeat_word(word, expected) -> None:
    assert repeat_word(word) == expected


@pytest.mark.parametrize(
    "arg1, arg2, arg3, expected",
    [(1, 2, 3, [1, 2, 3]), (0, 0, 0, [0, 0, 0]), (1, 1, 2, [1, 1, 2])],
)
def test_make_list(arg1, arg2, arg3, expected) -> None:
    ls = make_list(arg1, arg2, arg3)
    assert ls == expected


@pytest.mark.parametrize(
    "arg1, arg2, arg3, expected",
    [(1, 2, 3, (1, 2, 3)), (0, 0, 0, (0, 0, 0)), (1, 1, 2, (1, 1, 2))],
)
def test_make_tuple(arg1, arg2, arg3, expected) -> None:
    t = make_tuple(arg1, arg2, arg3)
    assert t == expected


@pytest.mark.parametrize(
    "arg",
    [
        {"name": "Ahmed", "age": 13, "car": "BMW"},
        {"name": "Khalid", "age": 30, "car": "Nissan"},
    ],
)
def test_make_dictionary1(arg) -> None:
    assert make_dictionary(**arg) == arg


def test_make_dictionary_no_order():
    assert make_dictionary(car="Toyota", age=25, name="Majed") == make_dictionary(
        name="Majed", age=25, car="Toyota"
    )
    assert make_dictionary(car="Toyota", age=25, name="Majed") != make_dictionary(
        "Toyota", 25, "Majed"
    )


@pytest.mark.parametrize(
    "number, ls, expected",
    [(1, [3, 5, 1], True), (2, [2], True), (3, [2, 1], False), (5, [], False)],
)
def test_find_number_in_list(number, ls, expected) -> None:
    assert find_number_in_list(number, ls) == expected


@pytest.mark.parametrize(
    "key, expected", [("one", 1), (1, "one"), ("hi", None), ("ls", [5, 7, 9])]
)
def test_find_value_of_key(key, expected, sample_dict) -> None:
    assert find_value_of_key(key, sample_dict) == expected
