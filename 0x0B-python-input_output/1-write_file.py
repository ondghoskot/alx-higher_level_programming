#!/usr/bin/python3
"""Defines a function write_file()"""


def write_file(filename="", text=""):
    """writes string to text file and returns the numbers of chars
        written"""
        with open(filename, "w", encoding="utf-8") as file2:
            return file2.write(text)
        return 0
