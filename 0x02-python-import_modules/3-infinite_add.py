#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1
    sum = 0
    if argc > 0:
        for i in range(1, argc + 1):
            sum += int(argv[i])
    print("{:d}".format(sum))
