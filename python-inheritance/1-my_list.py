#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


class MyList(list):
    """Class that inherits from list and can print itself sorted."""

    def print_sorted(self):
        """Print the list sorted in ascending order.

        The original list is not modified.
        """
        print(sorted(self))
