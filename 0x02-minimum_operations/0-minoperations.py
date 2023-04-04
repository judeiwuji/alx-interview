#!/usr/bin/python3
"""Module: Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of operations needed to
    result in exactly `n` `H` characters in the file"""

    ops = {'copyAll': 0, 'paste': 0}
    file_len = 1

    while file_len < n:
        if n % file_len == 0:
            ops['copyAll'] += 1
            clipboard = file_len
        ops['paste'] += 1
        file_len += clipboard
    return sum(ops.values())
