#!/usr/bin/python3
""" Return the peak in list """


def find_peak(list_of_integers):
    """ The function that returns peak """

    if type(list_of_integers) != list:
        return

    if len(list_of_integers) == 0:
        return None
    else:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
