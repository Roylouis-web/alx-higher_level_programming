#!/usr/bin/python3

import json

"""
    a function that returns the JSON
    representation of an object (string):
"""


def to_json_string(my_obj):
    """
    param my_obj: object parameter
    return: the JSON
    representation of an object (string)
    """

    return json.dumps(my_obj)
