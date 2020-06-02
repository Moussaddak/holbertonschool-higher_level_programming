#!/usr/bin/python3
""" Documentation of class Rectangle """


class Rectangle(BaseGeometry):
    """ subclass of BaseGeometry """

    def __init__(self, width, height):
        """ initiliazation methode """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
