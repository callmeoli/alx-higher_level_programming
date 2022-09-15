#!/usr/bin/python3
"""
    This module define square
"""


class Square:

    """ Class Square that defines a square.
    """
    def __init__(self, size=0):
        """Initialize method that stores the size of the square

        Args:
            param1 (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
