#!/usr/bin/python3
"""Defines unittests for models/square.py."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for Square class."""

    def test_square_methods(self):
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.area(), 25)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 5")
        s.size = 7
        self.assertEqual(s.width, 7)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")
        s.update(size=8, id=12, y=1, x=2)
        self.assertEqual(s.to_dictionary(), {"id": 12, "size": 8, "x": 2, "y": 1})


if __name__ == "__main__":
    unittest.main()
