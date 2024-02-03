#!/usr/bin/python3
"""Defines a function print_square"""


def print_square(size):
    """Prints a square using #

    Args:
        size: length of the square

    Raises:
        TypeError: if size isn't an integer
        ValueError: if size is less than 0

    Returns:
        nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")

    for i in range(size):
        print("{}".format("#" * size))
