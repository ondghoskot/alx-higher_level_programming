#!/usr/bin/python3
"""Defines a is_same_class function"""


def is_same_class(obj, a_class):
    """checks if the object is exactly an instance of the specified class

    Args:
        obj: object to check
        a_class: class of object

    Returns:
        True if the object is exactly an instance
        of the class or False otherwise
    """
    return type(obj) is a_class
