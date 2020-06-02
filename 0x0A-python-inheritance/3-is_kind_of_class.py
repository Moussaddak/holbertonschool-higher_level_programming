#!/usr/bin/python3
""" Documentation of Method is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class is a method that checks if the object is an instance of,
     or if the object is an instance of a class that inherited from,
      the specified class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
