#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass inheriting frm Rectangle"""
    def __init__(self, size):
        """initializing size frm width and height"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Description of square as string representation"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
