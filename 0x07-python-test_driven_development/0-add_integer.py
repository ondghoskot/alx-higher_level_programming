#!/usr/bin/python3
"""Defines a function: add_integer"""


def add_integer(a, b=98):
    """Adds two integers and returns result

    Args:
        a: first integer
        b: second integer
    Raises:
        TypeError: checks if a and b aren't integers or floats
    Return:
        sum of a and b
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
