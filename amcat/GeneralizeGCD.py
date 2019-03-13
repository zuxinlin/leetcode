#! /usr/bin/env python
# coding: utf-8

import collections


def find_gcd(x, y):
    while(y):
        x, y = y, x % y

    return x


def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    result = arr[0]

    for i in range(2, len(arr)):
        result = find_gcd(result, arr[i])

    return result


def main():
    assert generalizedGCD(5, [2, 3, 4, 5, 6]) == 1
    assert generalizedGCD(5, [2, 4, 6, 8, 10]) == 2


if __name__ == '__main__':
    main()
