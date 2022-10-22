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

    def area(self):

        """ Return:  The area of square """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ retrive size value"""
        return self.__size

    @size.setter
    def size(self, size):
        """ setter for size """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
