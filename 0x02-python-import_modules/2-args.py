#!/usr/bin/python3
import sys
if __name__ == "__main__":

    length = len(sys.argv)
    if length is 1:
        print("0 arguments.")
    elif length is 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(length - 1))
    for i in range(1, length):
        print("{:d}: {}".format(i, sys.argv[i]))
