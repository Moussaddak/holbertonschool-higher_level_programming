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
        return self.__height

    @height.setter
    def height(self, value):
        """ to set value of height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif isinstance(value, int) and value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ return value aera of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ return value perimeter of rectangle"""
        if not (self.__height and self.__width):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print a rectangle according to width and height"""
        r = ""
        if not (self.__height and self.__width):
            return r
        for i in range(self.__height):
            for j in range(self.__width):
                r += '#'
            r += '\n'
        r = r[:-1]
        return r
