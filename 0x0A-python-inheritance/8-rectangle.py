#!/usr/bin/python3
""" Documentation of class Rectangle """


class Rectangle(BaseGeometry):
    """ subclass of BaseGeometry """

    def __init__(self, width, height):
        """ initiliazation methode """
        self.__width = integer_validator(self, width)
        self.__height = integer_validator(self, height)
