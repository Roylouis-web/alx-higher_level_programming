#!/usr/bin/python3
"""module for use in writing json strings to files
"""


import json


def save_to_json_file(my_obj, filename):
    """saves obj to a file, overwriting previous contents
        -> handles NO exceptions
        -> encoded as utf-8
       Return: number of bytes written to file.
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(json.dumps(my_obj))


"""module for loading data from .json files
"""


def load_from_json_file(filename):
    """loads an object from json file containing json string
        -> handles NO exceptions
    """
    with open(filename, encoding='utf-8') as myFile:
        return (json.loads(myFile.read()))


def main():
    """contain main code in function
    """
    try:
        new_list = load_from_json_file('add_item.json')
    except:  # file didn't exist to read from
        new_list = []

    new_list.extend([sys.argv[i] for i in range(0, len(sys.argv)) if i != 0])
    try:
        save_to_json_file(new_list, 'add_item.json')
    except:
        pass


main()
