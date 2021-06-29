#!/usr/bin/env python
# -*- coding : utf-8 -*-


def primeFactors(n):
    prime_list = []
    for i in range(2, n+1):
        num = 0
        while n % i == 0:
            num += 1
            n /= i
        if num == 1:
            prime_list.append('(' + str(i) + ')')
        elif num > 1:
            prime_list.append('(' + str(i)+'**'+str(num) + ')')
        if n % i == n:
            return "".join(prime_list)


if __name__ == '__main__':
    result = primeFactors(7775460000)
    print(result)
