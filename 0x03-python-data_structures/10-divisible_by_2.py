#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            boolist += [True]
        else:
            boolist += [False]
        return boolist
