#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if not len(sys.argv) == 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = sys.argv[2]

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if ops is '+':
        result = add(a, b)
    elif ops is '-':
        result = sub(a, b)
    elif ops is '*':
        result = mul(a, b)
    elif ops is '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, ops, b, result))
