#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print()
        return
    for i in range(len(matrix)):
        lim = ' '
        for j in range(len(matrix[0])):
            if j == len(matrix[0]) - 1:
                lim = '\n'
            print("{:d}".format(matrix[i][j]), end=lim)
