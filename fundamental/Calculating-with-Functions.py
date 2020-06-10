#!/usr/bin/env python
# -*- coding : utf-8 -*-


# number
def zero(*args):
    length = len(args)
    if length == 0:
        return '0'
    elif length == 1:
        args[0].insert(0, '0')
        return eval(" ".join(args[0]))


def one(*args):
    length = len(args)
    if length == 0:
        return '1'
    elif length == 1:
        args[0].insert(0, '1')
        return eval(" ".join(args[0]))


def two(*args):
    length = len(args)
    if length == 0:
        return '2'
    elif length == 1:
        args[0].insert(0, '2')
        return eval(" ".join(args[0]))


def three(*args):
    length = len(args)
    if length == 0:
        return '3'
    elif length == 1:
        args[0].insert(0, '3')
        return eval(" ".join(args[0]))


def four(*args):
    length = len(args)
    if length == 0:
        return '4'
    elif length == 1:
        args[0].insert(0, '4')
        return eval(" ".join(args[0]))


def five(*args):
    length = len(args)
    if length == 0:
        return '5'
    elif length == 1:
        args[0].insert(0, '5')
        return eval(" ".join(args[0]))


def six(*args):
    length = len(args)
    if length == 0:
        return '6'
    elif length == 1:
        args[0].insert(0, '6')
        return eval(" ".join(args[0]))


def seven(*args):
    length = len(args)
    if length == 0:
        return '7'
    elif length == 1:
        args[0].insert(0, '7')
        return eval(" ".join(args[0]))


def eight(*args):
    length = len(args)
    if length == 0:
        return '8'
    elif length == 1:
        args[0].insert(0, '8')
        return eval(" ".join(args[0]))


def nine(*args):
    length = len(args)
    if length == 0:
        return '9'
    elif length == 1:
        args[0].insert(0, '9')
        return eval(" ".join(args[0]))


# mathematical operations
def plus(*args):
    return ["+", args[0]]


def minus(*args):
    return ["-", args[0]]


def times(*args):
    return ["*", args[0]]


def divided_by(*args):
    return ["//", args[0]]


if __name__ == '__main__':
    result = seven(times(five()))
    print(result)
