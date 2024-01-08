#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in range(len(my_string)):
        korok = my_string[i]
        if korok not 'c' and korok not 'C':
            new_string += korok
    return new_string
