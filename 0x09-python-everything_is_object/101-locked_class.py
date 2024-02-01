#!/usr/bin/python3
"""defines a class LockedClass"""


class LockedClass:
    """class that prevents the user from dynamically creating an attribute
        unless it's called first_name"""
        __slots__ = ["first_name"]
