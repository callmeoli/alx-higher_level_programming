#!/usr/bin/python3
""" Return the peak in list """


def find_peak(list_of_integers):
    """ The function that returns peak """

    if str(list_of_integers) == "[]":
        return None
    else:
        i = 0
        max_inx = i
        for i in range(len(list_of_integers)):
            if list_of_integers[i] > list_of_integers[max_inx]:
                max_inx = i
        return list_of_integers[max_inx]
