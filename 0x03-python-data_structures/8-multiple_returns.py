#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    if len(sentence) > 0:
        new_tuple = (len(sentence), sentence[0])
    else:
        None
    return new_tuple
