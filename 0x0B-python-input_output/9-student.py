#!/usr/bin/python3
""" This module contain class student """


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """"instantation of class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """"Return the dic represantion of class instance"""
        return self.__dict__
