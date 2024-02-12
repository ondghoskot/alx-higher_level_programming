#!/usr/bin/python3
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Subclass of Rectangle with private instance attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor to assign each arg with the right attr"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns string representatin of the class"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates the class' attributes"""
        attributes = ["id", "size", "x", "y"]

        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary reprsentation of the class"""
        dicty = {}
        attr = ["id", "size", "x"]
        for i in attr:
            dicty[i] = getattr(self, i)
        return dicty
