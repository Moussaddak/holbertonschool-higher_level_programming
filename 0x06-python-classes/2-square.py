#!/usr/bin/python3
"""define square class"""


class Square:

    """Initializes the square size."""
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
        finally:
            self.__size = size
