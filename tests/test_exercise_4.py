import pytest
from ihat_exercises.exercise_4 import extract_SIG_letters


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
