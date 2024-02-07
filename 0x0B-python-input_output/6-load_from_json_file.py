#!/usr/bin/python3
"""Defines function load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, "r", encoding="utf-8") as file5:
        return json.load(file5)
