#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":

    if not len(sys.argv) == 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = sys.argv[2]

    a = sys.argv[1]
    b = sys.argv[3]
    if ops is '+':
        result = add(int(a), int(b))
    elif ops is '-':
        result = sub(int(a), int(b))
    elif ops is '*':
        result = mul(int(a), int(b))
    elif ops is '/':
        result = div(int(a), int(b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
