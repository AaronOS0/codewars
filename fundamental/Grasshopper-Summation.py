#!/usr/bin/env python
# -*- coding : utf-8 -*-

from functools import reduce


def summation(num):
    return reduce(lambda x, y: x + y, range(num+1))


if __name__ == '__main__':
    result = summation(1)
    print(result)