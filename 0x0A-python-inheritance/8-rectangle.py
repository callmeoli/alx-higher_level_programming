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

    def area(self):
        """ calculate the area """"
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the input """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
