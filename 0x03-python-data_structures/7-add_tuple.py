#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        l = list(tuple_a)
        for i in range(2 - len(tuple_a)):
            l.append(0)
        tuple_a = tuple(l)
    if len(tuple_b) < 2:
        l = list(tuple_b)
        for i in range(2 - len(tuple_b)):
            l.append(0)
        tuple_b = tuple(l)
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
