#!/usr/bin/python3
"""Defines unittests for models/base.py."""
import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for Base class."""

    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_custom_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        res = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(res, str)
        self.assertEqual(res, '[{"id": 12}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        res = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(res, list)
        self.assertEqual(res, [{'id': 89}])


if __name__ == "__main__":
    unittest.main()
