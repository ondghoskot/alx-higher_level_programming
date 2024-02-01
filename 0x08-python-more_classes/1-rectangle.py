#!/usr/bin/python3
"""Defines a class called Rectangle"""


class Rectangle:
    """Rectangle defined its width and height"""
    def __init__(self, width=0, height=0):
        """
        Args:
            width: width of rectangle
            height: height of rectangle
        Raises:
            TypeError: checks if width and/or height isn't an int
            ValueError: checks if width and/or is less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @width.getter
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.getter
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
