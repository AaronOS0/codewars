#!/usr/bin/env python
# -*- coding : utf-8 -*-


def Xbonacci(signature, n):
    length = len(signature)
    [signature.append(sum(signature[-length:])) for i in range(length, n)]
    return signature[:n]


if __name__ == '__main__':
    new_signature = Xbonacci([1, 1, 1, 1], 10)
    print(new_signature)
