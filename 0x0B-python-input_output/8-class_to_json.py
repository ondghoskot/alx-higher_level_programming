#!/usr/bin/python3
"""Defines function to_json_string"""


def class_to_json(obj):
    """returns dictionary description for JSON sterialization of an object"""
    return obj.__dict__
