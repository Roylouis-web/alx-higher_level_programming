#!/usr/bin/python3
def add_integer(a, b=98):
    """
    adds an integer
    unit tests located in tests/0-add_integer.txt
    checks for type errors
    """
    if not type(a) == int:
        if type(a) == float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not type(b) == int:
        if type(b) == float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
