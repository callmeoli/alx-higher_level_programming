#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    sumi = 0
    for x in uniq:
        sumi = sumi + x
    return sumi
