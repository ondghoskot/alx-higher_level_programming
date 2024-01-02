#!/usr/bin/python3
def uppercase(str):
    uc = 0
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            uc = 32
        else:
            upper = 0
        print("{:c}".format(ord(c) - uc), end='')
    print(" ")
