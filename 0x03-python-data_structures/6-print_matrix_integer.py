#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) is 0:
        print()
        return
    for i in range(len(matrix)):
        for j in range(matrix[0]):
            print("{:d}".format(matrix[i][j], end=' '))
            if j == len(matrix[0]) - 1:
                print("{:d}".format(matrix[i][j], end='\n'))
