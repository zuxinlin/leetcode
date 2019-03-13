#! /usr/bin/env python
# coding: utf-8

import collections
import re

'''
Amazon is planning to release a new order prioritization algorithm to optimize fulfilling Prime deliveries on time. All orders (Prime or otherwise) are given an alphanumeric ID code. However, Prime orders are given additional metadata that consists of a space delimited list of lowercase English letters, whereas non-Prime orders are given metadata that consists only of a space delimited string of positive integers. Each order is therefore defined as their alphanumeric id code, followed by a space, followed by their space delimited metadata.

You have been tasked with sorting a list of all orders in the order queue to assist in prioritization of fulfillment. They should be sorted according to the following order:
1. The Prime orders should be returned first, sorted by lexicographic sort of the alphabetic metadata.
2. Only in the case of ties, the identifier should be used as a backup sort.
3. The remaining non-Prime orders must all come after, in the original order they were given in the input.

Write a function or method to sort the orders according to this system.
'''
def prioritizedOrders(numOrders, orderList):
    # WRITE YOUR CODE HERE
    prime_orders = []
    normal_orders = []

    for order in orderList:
        infos = order.split()

        if re.search('(^\d+$)', infos[1]):
            normal_orders.append(order)
        else:
            prime_orders.append(order)

    prime_orders.sort(key=lambda key: key.split(' ', 1)[1])

    return prime_orders + normal_orders


def main():
    print prioritizedOrders(
        4, ['mi2 jog mid pet', 'wz3 34 54 398', 'a1 alps cow bar', 'x4 45 21 7'])
    print prioritizedOrders(6, ['r1 box ape bit', 'br8 eat nim did',
                                'w1 has uni gry', 'b4 xi me nu', 't2 13 121 98', 'f3 52 54 31'])


if __name__ == '__main__':
    main()
    print re.search('(^\d+$)', '123')
    print re.search('(^\d+$)', '123abc')
