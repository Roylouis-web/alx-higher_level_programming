#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc > 1:
        print("{:d} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{:d}: {:s}".format(i, argv[i]))
    elif argc == 1:
        print("{:d} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{:d}: {:s}".format(i, argv[i]))
    elif argc == 0:
        print("{:d} arguments.".format(argc))
