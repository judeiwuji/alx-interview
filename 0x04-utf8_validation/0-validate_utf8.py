#!/usr/bin/python3
"""Module: UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding

    Args:
        data(list(int))
    """
    isValid = True

    for code in data:
        if code > 128 or code < -127:
            isValid = False
            break
    return isValid
