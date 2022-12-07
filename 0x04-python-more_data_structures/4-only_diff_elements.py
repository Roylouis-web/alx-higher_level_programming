#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set(set_1).difference(set_2)
    set_4 = set(set_2).difference(set_1)
    union = set(set_3).union(set_4)

    return union
