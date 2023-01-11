#!/usr/bin/python3


def read_file(filename=""):
    """reads a file
    """
    with open(filename, encoding='utf-8') as myFile:
        for lines in myFile:
            print(lines, end='')
