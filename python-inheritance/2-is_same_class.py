#!/usr/bin/python3
"""Module that defines a function that checks for the exact class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    return type(obj) is a_class
