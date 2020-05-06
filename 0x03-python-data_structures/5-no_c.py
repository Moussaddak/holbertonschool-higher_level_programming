#!/usr/bin/python3
def no_c(my_string):
    l = []
    for i in my_string:
        if i != 'C' and i != 'c':
            l.append(i)
    return (''.join(l))
