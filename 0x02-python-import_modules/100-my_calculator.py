#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    argc = len(sys.argv) - 1
    
    if argc == 3:
        argv = sys.argv
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        
        if op == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif op == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif op == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif op == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and / ")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
