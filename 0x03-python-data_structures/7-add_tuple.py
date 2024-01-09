#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = [0,0]
    i = 0

    while i < 2:
        if len(tuple_a) > i:
            sum[i] += tuple_a[i]
        if len(tuple_b) > i:
            sum[i] += tuple_b[i]
        i += 1
    return (sum[0], sum[1])
