#!/usr/bin/python3
"""documentation of method"""


class Square:
    """define square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not type(position) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (len(position) == 2 and type(position[0]) is int and
                  type(position[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (position[0] >= 0 and position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Retrieve the value of size (private object variable)"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size value of square"""
        print("No")
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate Area of the square"""
        return self.__size ** 2

    def my_print(self):
        """draw a square of # """
        if not self.__size:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """ set position value of Square"""
        if not type(value) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (len(value) == 2 and type(value[0]) is int and
                  type(value[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (value[0] > 0 and value[1] > 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        s = ''
        if not self.__size:
            return s
        for i in range(self.__position[1]):
            s += '\n'
        for i in range(self.__size):
            for j in range(self.__position[0]):
                s += " "
            for j in range(self.__size):
                s += "#"
            s += '\n'
        s = s[:-1]
        return s
