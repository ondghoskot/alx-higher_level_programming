#!/usr/bin/python3
"""script that adds all CLAs  to a python list and saves them to a file"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    cla = load_from_json_file("add_item.json")
except:
    cla = []
cla.extend(sys.argv[1:])
save_to_json_file(cla, "add_item.json")
