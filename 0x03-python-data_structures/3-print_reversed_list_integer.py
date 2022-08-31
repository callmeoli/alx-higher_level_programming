#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        print("", end="")
    else:
        i = len(my_list) + 1
        for i in range(1, i):
            print("{:d}".format(my_list[-i]))
