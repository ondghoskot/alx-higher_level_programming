#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    imax = my_list[0]
    for i in range(len(my_list)):
        if my_list[i + 1] > imax:
            imax = my_list[i + 1]
    return imax
