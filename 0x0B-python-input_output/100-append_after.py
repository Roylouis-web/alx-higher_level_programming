#!/usr/bin/python3
"""
a function that inserts a 
line of text to a file, after
each line containing specific
string
"""


def append_after(filename="", search_string="", new_string=""):
    """appends after search string instances in file
    """
    with open(filename, 'r', encoding='utf-8') as myFile:
        lines = myFile.readlines()

    for i, line in enumerate(lines):
        if search_string in line:
            lines.insert(i + 1, new_string)
    with open(filename, 'w', encoding='utf-8') as myFile:
        content = "".join(lines)
        myFile.write(content)
