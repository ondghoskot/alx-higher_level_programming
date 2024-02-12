#!/usr/bin/python3
"""Defines a class called Base"""


class Base:
    """class with a private attr, it will be
    the base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor that determines the id
        of the instance

        Args:
            id: the id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
