#!/usr/bin/python3
"""
    a function that writes a string
    to a text file (UTF8) and returns
    the number of characters written:
"""


def write_file(filename="", text=""):
    """
    param filename: source file
    param text: text to write to the
                source file.
    return: the number of characters written
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
