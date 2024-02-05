#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass inheriting frm Rectangle"""
    def __init__(self, size):
        """initializing size frm width and height"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Description of square"""
        return "[Square] {}/{}".format(self.__width, self.__height)