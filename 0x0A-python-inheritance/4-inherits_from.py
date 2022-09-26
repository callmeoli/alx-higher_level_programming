#!/usr/bin/python3
"""
This module check  if the object is an instance of,
or if the object is an instance of a class that
inherited from, the specified class ; otherwise False.
"""


def  inherits_from(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class
    Args:
        obj: object
        a_class: class type
    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
