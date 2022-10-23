#!/usr/bin/python3
""" This a function that returns
    the JSON representation of an object (string)
"""


import json


def load_from_json_file(filename):
    """ This function write file and return number of character written"""

    with open(filename, encoding='UTF-8') as f:
        JSON_file = json.load(f)
    return JSON_file
