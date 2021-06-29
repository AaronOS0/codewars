#!/usr/bin/env python
# -*- coding : utf-8 -*-
from collections import Counter
import itertools


def group(arr):
    counted_dict = Counter(arr)
    return [list(itertools.repeat(element[0], element[1])) for element in counted_dict.items()]


if __name__ == '__main__':
    result = group([3, 2, 6, 2, 1, 3])
    print(result)