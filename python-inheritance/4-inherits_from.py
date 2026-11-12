#!/usr/bin/python3
"""Module that defines a function that checks for a strict subclass."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    The object must not be an instance of a_class itself.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
