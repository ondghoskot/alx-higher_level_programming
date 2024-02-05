#!/usr/bin/python3
"""Defines a function lookup"""


def lookup(obj):
    """gets a list of all attributes and methods of a given object

    Args:
        obj: object to retrieve attributes and methods of

    Returns:
        a list of attributes and methods of obj
    """
    return dir(obj)
