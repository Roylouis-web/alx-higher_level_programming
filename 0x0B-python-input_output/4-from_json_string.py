#!/usr/bin/python3
import json

"""
     a function that returns an object
     (Python data structure) represented
     by a JSON string:
"""


def from_json_string(my_str):
    """
    param my_str: JSON String
    return: An object represented by
    a JSON String
    """

    return json.loads(my_str)
