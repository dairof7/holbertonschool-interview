#!/usr/bin/python3
"""
calculates the minimum amount of processes necessary
to create a certain number of characters.
"""


def minOperations(n):
    """
    Minimum Operations
    """
    if n <= 1:
        return 0
    num_operations = 0
    div = 2
    while n > 1:
        if n % div == 0:
            n /= div
            num_operations += div
        else:
            div += 1
    return num_operations
