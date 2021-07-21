def canUnlockAll(boxes):
    num_boxes = len(boxes)
    # keys = set([])
    keys = boxes[0]
    keys.append(0)
    # keys_open = [0]
    # key_set = set(keys)
    idx_key = 1
    # box_idx = list(range(1, num_boxes))
    # for i,boxkeys in enumerate(boxes):
    #     keys += boxkeys
    #     key_set = set(keys)
    #     print(key_set)
    # print('keys', keys)
    # print('box_idx', box_idx)
    for i in range(num_boxes-1):
        for j in range(idx_key, len(keys) + 1):
            # keys_open.append(j)
            keys = list(set(keys + boxes[j]))
            idx_key += 1
            # print('keys', keys)
            # print('keys_open', keys_open)
            i+=1
        else:
            if (len(keys)==num_boxes):
                return True
    else:
        return False
        # print('index', i)
