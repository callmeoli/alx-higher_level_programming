#!/usr/bin/python3
""" A rectangle with """


class Rectangle:
    """ A rectangle with a width and height. """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ (Rectangle, number, number) """

        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width

    def __str__(self):
        """ Return the value """

        str1 = ''
        if self.__width == 0 or self.__height == 0:
            return str1

        for height in range(self.__height):
            for width in range(self.__width):
                str1 += str(self.print_symbol)
            str1 += '\n'
        return str1

    def __repr__(self):
        """ Return the string represention """

        return ("Rectangle({0}, {1})".format(self.__width, self.__height))

    @property
    def width(self):
        """ (Rectangle, number, number) """
        return self.__width

    @width.setter
    def width(self, value):
        """ (Rectangle, number, number) """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ (Rectangle, number, number) """
        return self.__height

    @height.setter
    def height(self, value):
        """ (Rectangle, number, number) """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ calculate the area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ calculate the perimeter of rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __del__(self):
        """ Delete an instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
