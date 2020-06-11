#!/usr/bin/python3
def uppercase(str):
    s = ''
    for i in str:
        if ord(i) in range(97, 123):
            s += chr(ord(i) - 32)
        else:
            s += i
    print("{}".format(s))
