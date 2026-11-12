#!/usr/bin/python3
"""Module that defines a function that checks for a class or its parents."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of, or inherits from, a_class.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    return isinstance(obj, a_class)
