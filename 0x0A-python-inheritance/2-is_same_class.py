#!/usr/bin/python3
''' Documentation of Method is_same_class '''


def is_same_class(obj, a_class):
    ''' is_same_class is a method that checks if an object
     is an instance of a given class'''
    if type(obj) == a_class:
        return True
    else:
        return False
