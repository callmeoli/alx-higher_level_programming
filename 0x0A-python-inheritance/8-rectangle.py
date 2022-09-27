#!/usr/bin/python3
"""
This module include that print list in sorted order
"""


class BaseGeometry():
    """
    This class contain print sorted list
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
