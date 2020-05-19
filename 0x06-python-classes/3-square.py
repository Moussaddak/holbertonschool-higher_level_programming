#!/usr/bin/python3


class Square:
    """define square class"""
    def __init__(self, size=0):
        """Initializes the square size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate Area of the square"""
        return(self.__size ** 2)
