#!/usr/bin/python3
"""Module that defines a class Square with a private size."""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: the size of the square.
        """
        self.__size = size
