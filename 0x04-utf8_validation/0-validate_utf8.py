#!/usr/bin/python3
"""Module: UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding

    Args:
        data(list(int))
    """
    isValid = True

    for code in data:
        binary = bin(code).split("b")[1]
        oneByte = binary.startswith("0")
        twoBytes = binary.startswith("110")
        threeBytes = binary.startswith("1110")
        fourBytes = binary.startswith("11110")
        padding = binary.startswith("10")
        if not (oneByte or twoBytes or threeBytes or fourBytes or padding):
            isValid = False
            break
    return isValid
