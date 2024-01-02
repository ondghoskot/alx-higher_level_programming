#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if ld > 5 and number > 0:
    st = "greater than 5"
elif ld == 0:
    st = "0"
else:
    st = "less than 6 and not 0"
if number < 0:
    ld = -1 * ld
    print(f"Last digit of {number} is {ld} and is {st}")
else:
    print(f"Last digit of {number} is {ld} and is {st}")
