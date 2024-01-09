#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if sentence is None:
        fc = None
    fc = sentence[0]
    return (leng, fc)
