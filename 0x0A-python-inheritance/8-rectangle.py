#!/usr/bin/python3
""" Documentation of class Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ subclass of BaseGeometry """

    def __init__(self, width, height):
        """ initiliazation methode """
        self.__width = self.integer_validator(self, width)
        self.__height = self.integer_validator(self, height)
