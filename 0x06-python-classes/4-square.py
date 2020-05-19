#!/usr/bin/python3
"""documentation of method"""


class Square:
    """define square class"""
    def __init__(self, size=0):
        """Initializes the square size."""
        self.__size = size

    @property
    def size(self):
        """Retrieve the value of size (private object variable)"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """ set the size value of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate Area of the square"""
        return(self.__size ** 2)
