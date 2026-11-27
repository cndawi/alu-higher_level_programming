#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""
import io
import os
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for Rectangle class."""

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_instantiation(self):
        r1 = Rectangle(1, 2)
        self.assertEqual((r1.width, r1.height), (1, 2))
        r2 = Rectangle(1, 2, 3)
        self.assertEqual((r2.width, r2.height, r2.x), (1, 2, 3))
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual((r3.width, r3.height, r3.x, r3.y), (1, 2, 3, 4))
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area_str_dict(self):
        r = Rectangle(3, 4, 1, 2, 89)
        self.assertEqual(r.area(), 12)
        self.assertEqual(str(r), "[Rectangle] (89) 1/2 - 3/4")
        self.assertEqual(r.to_dictionary(),
                         {'id': 89, 'width': 3, 'height': 4, 'x': 1, 'y': 2})

    def test_display(self):
        buf = io.StringIO()
        sys.stdout = buf
        Rectangle(2, 2).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), "##\n##\n")

        buf = io.StringIO()
        sys.stdout = buf
        Rectangle(2, 2, 1).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), " ##\n ##\n")

        buf = io.StringIO()
        sys.stdout = buf
        Rectangle(2, 2, 1, 1).display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), "\n ##\n ##\n")

    def test_update_args_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(r.id, 1)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1)
        self.assertEqual(r.width, 1)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create_save_load(self):
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)
        r2 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r2.width, 1)
        r3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r3.height, 2)
        r4 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r4.x, 3)
        r5 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2,
                                 'x': 3, 'y': 4})
        self.assertEqual(r5.y, 4)

        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual((loaded[0].width, loaded[0].height), (1, 2))


if __name__ == "__main__":
    unittest.main()
