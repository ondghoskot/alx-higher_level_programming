#!/usr/bin/python3
"""Defines class **Square** by a private size attribute"""


class Square:
    """Define square"""
    def __init__(self, size=0):
        """special init method to define private instance size attribute

            Args:
                size: integer that represents the size of the square.

            Raises:
                TypeError: if size is not an integer.
                ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """calculates area of Square."""
            return self.__size ** 2
