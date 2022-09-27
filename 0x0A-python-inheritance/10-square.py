#!/usr/bin/python3
"""
This module include that print list in sorted order
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class contain print sorted list
    """

    def __init__(self, size):
        """ Initializes instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ a method that return the area of the instance """
        return super().area()
