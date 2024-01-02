#!/usr/bin/python3
def uppercase(str):
    uc = 0
    for l in str:
        if ord(l) >= ord('a') and ord(l) <= ord('z'):
            uc = 32
        else:
            upper = 0
        print("{:c}".format(ord(l) - uc), end='')
    print("")
