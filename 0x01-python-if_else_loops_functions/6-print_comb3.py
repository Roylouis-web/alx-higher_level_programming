#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i > j or i == j:
            continue
        elif i < 8:
            print("{:d}{:d}, ".format(i, j), end='')
        else:
            print("{:d}{:d}".format(i, j))
