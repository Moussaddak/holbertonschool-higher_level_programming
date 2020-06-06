#!/usr/bin/python3
""" mothod of Pascal's triangle """


def f(n):
    """ factorial function """
    r = 1
    if not n:
        return 1
    for i in range(1, n + 1):
        r = r * i
    return r


def C(k, l):
    """  binomial coefficients function"""
    return int(f(k) / (f(l) * f(k - l)))


def pascal_triangle(n):
    """ Pascal's triangle """
    k = []
    if n <= 0:
        return []
    for i in range(n):
        l = []
        for j in range(i + 1):
            l.append(C(i, j))
        k.append(l)
    return k
