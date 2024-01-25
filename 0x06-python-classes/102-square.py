#!/usr/bin/python3
"""Defines class **Square** by a private size attribute"""


class Square:
    """Define square"""
    def __init__(self, size=0):
        """special init method to define private instance size attribute

            Args:
                size: integer that represents the size of the square.
        """
        self.__size = size
        
    @property
    def size(self):
        """the getter method in order to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """the setter method for setting the size

            Args:
                value: integer representing the size of the square

            Raises:
                TypeError: if size is not an integer.
                ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates area of Square."""
        return self.__size ** 2
