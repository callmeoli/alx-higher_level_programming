#!/usr/bin/python3
"""
    This module define square
"""


class Square:

    """ Class Square that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
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
        if not isinstance(position, tuple) or not len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """ Retrive postion value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of `position`
        Args:
            value (int): value to be set to `position` attribute
        Raise:
            TypeError: position isn't a tupple or doesn't contain 2
                       elements or has negative integers
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
            return

        [print() for i in range(self.position[1])]
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
