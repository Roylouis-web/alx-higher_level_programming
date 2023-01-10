#!/usr/bin/python3
"""
 an attribute to the class if possible
         -> aka is
"""


def add_attribute(obj, name, value):
    """adds an attribute to the class if possible
        -> aka is
    """
    builtins = (str, int, complex, bool, float, list,
                tuple, dict, set, frozenset, type, object)
    for _type in builtins:
        if type(obj) is _type:
            raise TypeError("can't add new attribute")

    object.__setattr__(obj, name, value)
