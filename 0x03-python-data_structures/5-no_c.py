#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    new_string = ""
    for i in range(len(my_string)):
        korok = my_string[i]
        if korok not in 'cC':
            new_string += korok
    return new_string
