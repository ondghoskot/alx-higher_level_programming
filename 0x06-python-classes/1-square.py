#!/usr/bin/python3
"""Defines class **Square** by a private size attribute"""


class Square:
    """Define square"""
    def __init__(self, size):
        """special init method to define private instance size attribute

            Args:
                size: integer that represents the size of the square.
        """
        self.__size = size
