#!/usr/bin/python3
"""
calculates the minimum amount of processes necessary
to create a certain number of characters.
"""


def minOperations(n):
    """
    Min Operations
    Args:
        n (int): number of copies
    Returns:
        [int]: [minimun operations]
    """
    i = int(n/2)
    ac = 0
    num = n
    while num > 1:
        while num % i != 0:
            i -= 1
            if i == 0:
                return n
        ac += num / i
        num = num/(num / i)
        i -= 1
    return int(ac)