#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """class with 3 public instance attributes"""
    def __init__(self, first_name, last_name, age):
        """instantiation of the public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict representation of an instance"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        if isinstance(attrs, list):
            for strgs in attrs:
                if isinstance(strgs, str) and strgs in self.__dict__:
                    new_dict[strgs] = self.__dict__[strgs]
            return new_dict
