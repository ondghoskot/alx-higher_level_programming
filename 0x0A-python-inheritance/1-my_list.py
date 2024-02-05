#!/usr/bin/python3
"""Defines a class called Mylist that inherits from list obj"""


class MyList(list):
    """Uses a public instance method print_sorted"""

    def print_sorted(self):
        """sorts a list of ints and prints it"""
        print(sorted(self))
