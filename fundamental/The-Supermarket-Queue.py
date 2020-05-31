#!/usr/bin/env python
# -*- coding : utf-8 -*-


def queue_time(customers, n):
    # in case the empty customers
    customers.append(0)
    t = 0
    # the number of customer <= the number of tills
    if len(customers) <= n:
        longest_time = max(customers)
    else:
        # initialize a "Double Dimensional Array":[[], [], ...]
        till = [[] for i in range(n)]
        # fill the array by customers
        for customer in customers[:n]:
            till[t].append(customer)
            t += 1
        # the next customer always after the shortest time in the array
        for customer in customers[n:]:
            till = sorted(till, key=sum)
            till[0].append(customer)
        till = sorted(till, key=sum)
        longest_time = sum(till[-1])
    return longest_time


if __name__ == '__main__':
    result = queue_time([27, 16, 10, 18, 15, 42, 33, 48, 23, 34, 36, 2], 3)
    print(result)




