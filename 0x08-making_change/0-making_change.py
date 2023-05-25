#!/usr/bin/python3
"""Module: makeChange"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to
    meet a given amount total

    Args:
     coins: list(int)
     total: int
    """
    if total <= 0:
        return 0
    d = coins[:]
    totalChange = 0
    count = 0
    while totalChange < total and len(d) > 0:
        change = max(d)
        if change + totalChange <= total:
            totalChange += change
            count += 1
        else:
            d.remove(change)
    return count if totalChange == total else -1
