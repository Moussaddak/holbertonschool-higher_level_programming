#!/usr/bin/python3
def uppercase(str):
    s = ''
    for i in str:
        if ord(i) in range(65, 91):
            s += i
        elif ord(i) in range(97, 123):
            s += chr(ord(i) - 32)
    print(s)
