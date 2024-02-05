#!/usr/bin/python3
"""Defines a is_kind_of__class function"""


def is_same_class(obj, a_class):
    """checks if the object is an instance of the specified class or its subclass

    Args:
        obj: object to check
        a_class: class of object

    Returns:
        True if the object is an instance
        of the class or subclass or False otherwise
    """
    return isinstance(obj, a_class)
