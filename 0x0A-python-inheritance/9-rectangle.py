#!/usr/bin/python3
"""Defines a subclass Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns a description for the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
