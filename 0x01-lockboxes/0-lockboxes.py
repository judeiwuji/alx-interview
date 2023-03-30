#!/usr/bin/python3
"""Module:  Lockboxes"""


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked

    Args:
        boxes:(list)
    """
    unlocked = {}
    unlockCount = 0

    for i, box in enumerate(boxes):
        if len(box) == 0 and i + 1 == len(boxes):
            unlockCount += 1
        for key in box:
            if key < len(boxes):
                door = unlocked.get(key, None)
                if door is None:
                    unlocked[key] = key
                    unlockCount += 1
    # print(unlocked)
    return unlockCount == len(boxes)
