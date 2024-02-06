#!/usr/bin/python3
"""Defines a read_file() function"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8"):
        print(filename.read())
