#!/usr/bin/env python
# -*- coding : utf-8 -*-


def tribonacci(signature, n):
        [signature.append(sum(signature[-3:])) for i in range(3, n)]
        return signature[:n]


if __name__ == '__main__':
    new_signature = tribonacci([1, 1, 1], 10)
    print(new_signature)