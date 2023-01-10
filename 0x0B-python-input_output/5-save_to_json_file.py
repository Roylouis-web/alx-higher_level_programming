#!/usr/bin/python3
import json

"""
    a function that writes an Object
    to a text file, using a JSON representation:
"""


def save_to_json_file(my_obj, filename):
    """
    param my_obj: object parameter
    param filename: a text file parameter
    return: Nothing
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
