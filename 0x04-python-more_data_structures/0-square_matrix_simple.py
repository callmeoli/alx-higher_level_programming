#!/usr/bin/python3
def square(x):
    return x*x
def square_matrix_simple(matrix=[]):
    new_matrix = map(square, matrix)
    return new_matrix