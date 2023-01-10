#!/usr/bin/python3
"""
     a function that reads a text
     file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    param filename: source file
    return: Nothing
    """

    with open(filename, mode='r', encoding='utf-8') as f:
        for lines in f:
            print(lines, end='')
