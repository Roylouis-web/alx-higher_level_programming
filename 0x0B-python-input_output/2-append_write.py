#!/usr/bin/python3
"""
    a function that appends a
    string at the end of a text file
    (UTF8) and returns the number
    of characters added:
"""


def append_write(filename="", text=""):
    """
    param filename:
    param text: file to be appended with a
                new text
    return: the number of characters added
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
