#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng:
        fc = sentence[0]
    else:
        fc = None
    return (leng, fc)
