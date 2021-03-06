#!/usr/bin/python3
"""
    Documentation of method
    definition of an empty class
"""


class Rectangle:
    """ define a Rectangle Class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve value of width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """ to set value of width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif isinstance(value, int) and value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ retrieve value of height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """ to set value of height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif isinstance(value, int) and value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
