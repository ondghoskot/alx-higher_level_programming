#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    leng = len(argv)
    if leng != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if op == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif op == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
