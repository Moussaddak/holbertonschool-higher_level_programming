#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for i in range(0, len(str)):
        if i != n:
            s += str[i]

    return s
