#!/usr/bin/python3
"""Defines class MyInt"""


class MyInt(int):
    """subclass of int that has == and != inverted"""
    def __eq__(self, other):
        """Returns True if slef != other"""
        return int(self) != other

    def __ne__(self, other):
        """Returns False if self == other"""
        return int(self) == other
