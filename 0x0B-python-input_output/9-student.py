#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """class with 3 public instance attributes"""
    def __init__(self, first_name, last_name, age):
        """instantiation of the public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict representation of an instance"""
        return self.__dict__
