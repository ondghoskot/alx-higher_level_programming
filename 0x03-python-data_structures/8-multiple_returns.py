#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng is 0:
        fc = None
    fc = sentence[0]
    return (leng, fc)
