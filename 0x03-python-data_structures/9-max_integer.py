#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maxm = my_list[0]
        for i in range(0, len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                maxm = my_list[i]
                return maxm
