#!/usr/bin/python3
"""Defines a inherits_frm function"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a subclass of the
    specified class

    Args:
        obj: object to check
        a_class: class of object

    Returns:
        True if the object is an instance
        of the subclass or False otherwise
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
