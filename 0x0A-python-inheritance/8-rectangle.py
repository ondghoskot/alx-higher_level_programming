#!/usr/bin/python3
"""Defines a subclass Rectangle"""


class Rectangle(BaseGeometry):
    """subclass that has two private attributes height and width

    Args:
        width: width of rectangle
        height: height of rectangle
    """
    def __init__(self, width, height):
        """validates width and height using the superclass' method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
