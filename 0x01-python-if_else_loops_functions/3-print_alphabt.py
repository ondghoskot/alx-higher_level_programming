#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if a == ord('q') or a == ord('e'):
        a += 1
    else:
        print("{:c}".format(a), end='')
