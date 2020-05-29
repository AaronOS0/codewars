#!/usr/bin/env python
# -*- coding : utf-8 -*-


def productFib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    return [a, b, a * b == prod]


if __name__ == '__main__':
    result = productFib(5895)
    print(result)

