#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = []
    for i in range(0, len(tuple_a)):
        if len(tuple_b) == 0:
            tuple_c.append(tuple_a[i])
        elif len(tuple_b) == 1:
            if i == 0:
                tuple_c.append(tuple_a[i] + tuple_b[i])
            else:
                tuple_c.append(tuple_a[i])
        else:
            tuple_c.append(tuple_a[i] + tuple_b[i])
    return tuple(tuple_c)
