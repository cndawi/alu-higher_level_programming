#!/usr/bin/python3
"""Module that defines a class Square with an area method."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): the size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
