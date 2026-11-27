#!/usr/bin/python3
"""Defines unittests for models/base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittests for Base class."""

    def tearDown(self):
        for fn in ("Rectangle.json", "Square.json", "Base.json",
                   "Rectangle.csv", "Square.csv"):
            try:
                os.remove(fn)
            except IOError:
                pass

    def test_id_auto_and_custom(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, b2.id + 1)

    def test_to_json_string(self):
        self.assertEqual("[]", Base.to_json_string(None))
        self.assertEqual("[]", Base.to_json_string(list()))
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string(list((r.to_dictionary(),)))))

    def test_from_json_string(self):
        self.assertEqual(list(), Base.from_json_string(None))
        self.assertEqual(list(), Base.from_json_string("[]"))
        inp = list(({"id": 89, "width": 10, "height": 4},))
        out = Base.from_json_string(Base.to_json_string(inp))
        self.assertEqual(inp, out)

    def test_save_and_load_file(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file(list((r1,)))
        loaded = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(loaded.__getitem__(0)))

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)


if __name__ == "__main__":
    unittest.main()
