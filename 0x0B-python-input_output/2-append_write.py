#!/usr/bin/python3
"""Defines a function append_write()"""


def write_file(filename="", text=""):
    """appends string to end of file and returns the numbers of characs written"""
    with open(filename, "a", encoding="utf-8") as file3:
        return file3.write(text)
