#!/usr/bin/python3
"""Defines a function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

        Args:
            first_name: <first name>
            las_name: <last_name>

        Raises:
            TypeError: if one of the args isn't a string

        Returns:
            nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
