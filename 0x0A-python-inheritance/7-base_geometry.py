#!/usr/bin/python3
""" Documentation of class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate the entry value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
