#!/usr/bin/python3
"""Defines function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file using json representation"""
    with open(filename, "w", encoding="utf-8") as file4:
        return json.dump(my_obj, file4)
