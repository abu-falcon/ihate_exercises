import pytest
from ihat_exercises.exercise_4 import (
    combine_two_lists,
    connect_strings_with_seperator,
    count_nonempty_lines_file,
    extract_SIG_letters,
    get_element_and_index,
)


@pytest.fixture
def fake_file(tmp_path):
    def inner(lines):
        file = tmp_path / "fake.txt"
        nonempty_lines_count = len([line for line in lines if line.strip() != ""])
        file.write_text("\n".join(lines))
        return str(file), nonempty_lines_count

    return inner


@pytest.mark.parametrize(
    "d, expected",
    [
        (
            {
                "heSIGabc": "a",
                "sigabc": "b",
                "SIGABc": "c",
                "SIGab3": "d",
                "SIBabc": "e",
                "SIGa": "f",
                "SIG": "g",
                "SIGk11111A": "h",
            },
            [("c", "SIGABc"), ("d", "SIGab3"), ("f", "SIGa"), ("h", "SIGk11111A")],
        ),
        ({"SIG111": "hi"}, []),
        ({"SIGXY": "xy", "SIG": "y"}, [("xy", "SIGXY")]),
        ({}, []),
    ],
)
def test_extract_SIG_letters(d, expected):
    assert extract_SIG_letters(d) == expected


@pytest.mark.parametrize(
    "iter1, iter2, expected",
    [
        ([1, 2, 3], [4, 5, 6], [(1, 4), (2, 5), (3, 6)]),
        ("hello", "hi", [("h", "h"), ("e", "i")]),
        (range(10), range(20), list(zip(range(10), range(20)))),
        ("Yes", range(5), [("Y", 0), ("e", 1), ("s", 2)]),
        ([], "no", []),
    ],
)
def test_combine_two_lists(iter1, iter2, expected):
    assert combine_two_lists(iter1, iter2) == expected


@pytest.mark.parametrize(
    "iter, expected",
    [
        (("apple", "banana", "mango"), [(0, "apple"), (1, "banana"), (2, "mango")]),
        (range(2), [(0, 0), (1, 1)]),
        ("", []),
        (["hi", "hello"], list(zip(range(2), ["hi", "hello"]))),
    ],
)
def test_get_element_and_index(iter, expected):
    assert get_element_and_index(iter) == expected


@pytest.mark.parametrize(
    "strings, sep, expected",
    [
        (["I", "love", "Coca-Cola"], " ", "I love Coca-Cola"),
        ("YouAreKind", "/,", "Y/,o/,u/,A/,r/,e/,K/,i/,n/,d"),
        (("1", "2", "3"), " | ", "1 | 2 | 3"),
        ((str(elem) for elem in range(7, 9)), "??", "7??8"),
    ],
)
def test_connect_strings_with_seperator(strings, sep, expected):
    assert connect_strings_with_seperator(strings, sep) == expected


@pytest.mark.parametrize(
    "strings",
    [
        ["   ", "\n\n\n", "hii\n", "\n\n \n\n", "hi"],
        ["1", "2", "3", "\t\t?", "5"],
        [" "],
        1000 * ["     "],
        ["\t\t\tgfdgf\n\n\n\n"],
    ],
)
def test_count_nonempty_lines_file(fake_file, strings):
    file, nonempty_lines_count = fake_file(strings)
    assert count_nonempty_lines_file(file) == nonempty_lines_count
