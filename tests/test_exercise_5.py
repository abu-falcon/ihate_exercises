import pytest
from ihat_exercises.exercise_5 import Square


@pytest.fixture
def squares():
    return [Square(i, 9 - i) for i in range(10)]


class TestSquare:
    def test_init(self, squares):
        first, second, *_, before_last, last = squares
        assert hasattr(first, "id")
        assert hasattr(second, "side")
        assert first.id == 0 and first.side == 9
        assert last.id == 9 and last.side == 0

    def test_get_area(self, squares):
        first, *_, last = squares
        assert first.get_area() == 81
        assert last.get_area() == 0

    def test_change_id(self, squares):
        middle = squares[4]
        middle.change_id(40)
        assert middle.id == 40

    def test_expand_side(self, squares):
        sq = squares[8]
        sq.expand_side(2)
        assert sq.side == 2
        sq.expand_side(2)
        assert sq.side == 4

    def test_str(self, squares):
        first = squares[0]
        assert str(first) == "Square(id=0, side=9.00)"
        first.change_id(10)
        first.expand_side(0)
        assert str(first) == "Square(id=10, side=0.00)"

    def test_is_bigger(self, squares):
        first, *_, last = squares
        assert first.is_bigger(last)
        assert Square(100, 99.99).is_bigger(Square(50, 99))

    def test_gt(self, squares):
        assert squares[7] > squares[4]
        assert Square(50, 20) > Square(49, 10000)
