#!/usr/bin/python3
"""Defines class MyInt"""


class MyInt(int):
    """subclass of int that has == and != inverted"""
    def __el__(self, other):
        """Returns True if slef != other"""
        return int(self) != other

    def __nl__(self, other):
        """Returns True if sekf == other"""
        return int(self) == other
