#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    str = ''
    max = max(a_dictionary.values(), default=None)
    for i in a_dictionary:
        if a_dictionary[i] > max:
            max = a_dictionary[i]

    for i in a_dictionary:
        if a_dictionary[i] == max:
            str = i
    return str
