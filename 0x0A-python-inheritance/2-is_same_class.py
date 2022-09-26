#!/usr/bin/python3
"""
This module include a function that returns True if the
object is exactly an instance of the specified class
otherwise False.
"""


def is_same_class(obj, a_class):
    """
     This function check if obj is instance of a_class
    """

    return type(obj) is a_class
