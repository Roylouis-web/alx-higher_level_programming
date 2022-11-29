#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i > j or i == j:
            continue
        elif i < 8:
            print(f"{i}{j}, ", end='')
        else:
            print(f"{i}{j}\n")
