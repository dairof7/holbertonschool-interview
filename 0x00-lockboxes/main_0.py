#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))


boxes = [[3, 8,8,2,3,8,9], [2], [0, 1], [4], [5], [4, 1], [1, 6]]
print(canUnlockAll(boxes))
    #    [0]  [1]     [2]     [3]   [4]    [5]      [6]      [7]
boxes = [[]]
print(canUnlockAll(boxes))

2,3,1,4