#!/usr/bin/python3


def read_file(filename=""):
    """reads a text file (UTF-8)
        and prints it to stdout
    """

<<<<<<< HEAD
    with open(filename, mode='r', encoding='utf-8') as myFile:
=======
    with open(filename, mode= 'r', encoding='utf-8') as myFile:
>>>>>>> c03e75aa838a436cd05cb552c09c1bd864824534
        for lines in myFile:
            print(lines, end='')
