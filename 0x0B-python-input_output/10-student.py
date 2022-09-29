#!/usr/bin/python3
""" This module contain class student """


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """"instantation of class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"Return the dic represantion of class instance"""
        dict_rep = self.__dict__
        if attrs is None:
            return dict_rep

        d= {k: v for k, v in dict_rep.items() if k in attrs}
        return d
