#!/usr/bin/env python
# -*- coding : utf-8 -*-


def find_even_index(arr):
    arr.insert(0, 0)
    arr_len = len(arr)
    # Compare the summation from left and side with index
    index = [i for i in range(0, arr_len) if sum(arr[:i]) == sum(arr[i+1:])]
    if index and index[0] > 0:
        return index[0] - 1
    elif not index:
        return -1
    else:
        return index[0]


if __name__ == '__main__':
    N = find_even_index(list(range(-100,-1)))
    print(N)
