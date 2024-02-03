#!/usr/bin/python3
"""Defines a function matrix_divided"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix
    Args:
        matrix: the matrix to use
        div: the number to divide the elements by
    Raises:
        TypeError: if the elements of the matrix are not integers or floats
            or rows of the matrix aren't the same size
            or div isn't a number
        ZeroDivisionError: if div is equal to 0
    Returns:
        a new matrix
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not (isinstance(matrix, list) or matrix) or len(matrix) == 0:
        raise TypeError(error)

    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError(error)
        for i in rows:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError(error)
        if len(rows) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in rows] for rows in matrix]
