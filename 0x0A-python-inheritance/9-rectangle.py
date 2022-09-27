#!/usr/bin/python3
"""
This module include that print list in sorted order
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class contain print sorted list
    """

    def __init__(self, width, height):
        """ Initializes instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """Validate the input """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
    def area(self):
        """ a method that return the area of the instance """
        return self.__width * self.__height
    def __str__(self):
        """ Special metho that return the printable string """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
