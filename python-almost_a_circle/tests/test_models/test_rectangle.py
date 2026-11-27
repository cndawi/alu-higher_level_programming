#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""
import io
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for Rectangle class."""

    def test_init_and_validation(self):
        r = Rectangle(10, 2, 1, 3, 99)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (10, 2, 1, 3, 99))
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_area_str_display(self):
        r = Rectangle(3, 2, 1, 1, 5)
        self.assertEqual(r.area(), 6)
        self.assertEqual(str(r), "[Rectangle] (5) 1/1 - 3/2")
        buf = io.StringIO()
        sys.stdout = buf
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), "\n ###\n ###\n")

    def test_update_and_dict(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")
        r.update(x=1, height=2, y=3, width=4, id=90)
        self.assertEqual(r.to_dictionary(), {"id": 90, "width": 4, "height": 2, "x": 1, "y": 3})


if __name__ == "__main__":
    unittest.main()
