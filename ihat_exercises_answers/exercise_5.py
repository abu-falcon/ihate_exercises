from __future__ import annotations


class Square:
    def __init__(self, id: int, side: float) -> None:
        "set :attr:`id` and :attr:`side` so they are accessible in the methods"
        self.id = id
        self.side = side

    def get_area(self) -> float:
        ":meth:`get_area` calculates the area of the square"
        return self.side**2

    def change_id(self, new_id: int) -> None:
        "change :attr:`id` to the new id"
        self.id = new_id

    def expand_side(self, factor: float) -> None:
        "increase :attr:`side` by a factor"
        self.side = factor * self.side

    def __str__(self) -> str:
        """
        when you print the instance, make it look the following:
            "Square(id=x, side=y)"
            where,
                x is the actual id
                y is the actual side length rounded to two decimal digits
        """
        return f"Square(id={self.id}, side={self.side:.2f})"

    def is_bigger(self, other_square: Square) -> bool:
        """
        check if the area of instance is bigger than the area of another square instance

        """
        return self.get_area() > other_square.get_area()

    def __gt__(self, other_square: Square) -> bool:
        """
        This is (g)reater (t)han [>] comparison
        Compare them by id
        """
        return self.id > other_square.id
