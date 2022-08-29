#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or len(my_list) <= idx:
        return my_list
    else:
        my_list.remove(my_list[idx])
        new_list = my_list
        return new_list
