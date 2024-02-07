#!/usr/bin/python3
"""Defines a function append_write()"""


def append_write(filename="", text=""):
    """appends string to end of file and returns the numbers of chars written"""
    with open(filename, "a", encoding="utf-8") as file3:
        return file3.write(text)
