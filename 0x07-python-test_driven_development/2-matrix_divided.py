#!/usr/bin/python3
"""
This module is composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """
    len_row = []
    i = 0
    j = 0
    new_mat = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError
                (
                    "matrix must be a matrix (list of lists)\
                     of integers/floats"
                    )
            # new_mat[i][j] = round((matrix[i][j] / div), 2)
        len_row.append(j)

    for i in range(len(len_row) - 1):
        if len_row[i] != len_row[i + 1]:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_mat = list(
                map(lambda x: list(map
                    (lambda y: round(y / div, 2), x)), matrix))

    return new_mat
