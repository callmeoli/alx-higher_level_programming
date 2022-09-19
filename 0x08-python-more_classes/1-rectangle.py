#!/usr/bin/python3
""" A rectangle with """


class Rectangle:
    """ A rectangle with a width and height. """
    def __init__(self, width=0, height=0):
        """ (Rectangle, number, number) """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ (Rectangle, number, number) """
        return self.__width

    @property
    def height(self):
        """ (Rectangle, number, number) """
        return self.__height

    @width.setter
    def width(self, value):
        """ (Rectangle, number, number) """
        self.__width = value

    @height.setter
    def height(self, value):
        """ (Rectangle, number, number) """
        self.__height = value
