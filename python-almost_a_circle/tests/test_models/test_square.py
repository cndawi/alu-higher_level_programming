#!/usr/bin/python3
"""Defines unittests for models/square.py."""
import os
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for Square class."""

    def tearDown(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_instantiation(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        s2 = Square(1, 2)
        self.assertEqual((s2.size, s2.x), (1, 2))
        s3 = Square(1, 2, 3)
        self.assertEqual((s3.size, s3.x, s3.y), (1, 2, 3))
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.id, 4)

    def test_errors(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_dict_update(self):
        s = Square(2, 1, 3, 89)
        self.assertEqual(str(s), "[Square] (89) 1/3 - 2")
        self.assertEqual(s.to_dictionary(),
                         {'id': 89, 'size': 2, 'x': 1, 'y': 3})

        s.update()
        self.assertEqual(s.id, 89)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1)
        self.assertEqual(s.size, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_save_load(self):
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)
        s2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s2.size, 1)
        s3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s3.x, 2)
        s4 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s4.y, 3)

        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([Square(1)])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].size, 1)


if __name__ == "__main__":
    unittest.main()
