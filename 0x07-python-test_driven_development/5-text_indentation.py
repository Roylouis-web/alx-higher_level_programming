#!/usr/bin/python3
"""
 python program to print an
 indented string
 """


def text_indentation(text):
    """
    prints a string of text with 2 new lines after '.', '?', and ':'
    unit tests located in tests/5-text_indentation.txt
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    specials = ['.', '?', ':']
    for ch in text:
        string += ch
        if ch in specials:
            string += "\n\n"
    print(string, end='')
