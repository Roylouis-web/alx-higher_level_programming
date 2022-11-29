#!/usr/bin/python3
def uppercase(str):
    out = ''
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            l = ord(i) - 32
            out += chr(l)
        else:
            out += i
    print("{:s}".format(out))
