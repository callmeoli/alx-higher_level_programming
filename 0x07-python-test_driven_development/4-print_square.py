#!/usr/bin/python3
"""
    This module contians function that print square
"""


def print_square(size):
    """Print square with the size """

    if type(size) != int or (type(size) == float and size > 0):
        raise TypeError("size must be an integer")
    if size < 0 and type(size) != float:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    size = int(size) if isinstance(size, float) else size
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
