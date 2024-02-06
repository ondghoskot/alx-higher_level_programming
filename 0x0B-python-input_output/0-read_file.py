#!/usr/bin/python3
"""Defines a read_file() function"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file1:
        print(file1.read(), end="")
