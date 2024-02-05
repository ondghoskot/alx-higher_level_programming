#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """class defined with a public instance method"""
    def area(self):
        """public instance method that finds the area"""
        raise Exception("area() is not implemented")

    def integer_validator(slef, name, value):
        """Method that validates value

        Args:
            name: string representing the name of integer
            value: value of the integer

        Raises:
            TypeError: if value is not an integer
            ValyeError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
