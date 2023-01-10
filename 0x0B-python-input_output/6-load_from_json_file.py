#!/usr/bin/python3
"""
    a function that creates
    an Object from a “JSON file”:
"""


def load_from_json_file(filename):
    """
    param filename: A JSON file
    return: returns a python Object
    """

    with open(filename, encoding='utf-8') as f:
        return eval(f.read())
