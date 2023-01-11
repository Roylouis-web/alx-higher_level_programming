#!/usr/bin/python3


def read_file(filename=""):
    """reads a text file (UTF-8)
        and prints it to stdout
    """

    with open(filename, mode='r', encoding='utf-8') as myFile:
        for lines in myFile:
            print(lines, end='')
