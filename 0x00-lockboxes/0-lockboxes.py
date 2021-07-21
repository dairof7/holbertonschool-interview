#!/usr/bin/python3
"""
canUnlockAll module
"""


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    keys = [0] + boxes[0]
    for i in range(num_boxes-1):
        for j in keys[1:]:
            if j <= num_boxes + 1:
                keys = list(set(keys + boxes[j]))
                i += 1
        else:
            if (len(keys) >= num_boxes):
                return True
    else:
        if num_boxes == 1:
            return True
        else:
            return False
