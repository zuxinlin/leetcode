#! /usr/bin/env python
# coding: utf-8

"""
线性查找
"""

from random import sample, randint


def find(arr, target):
    """
    给定一个数组和目标数，查找这个数是否在数组中，在的话返回下标，不在返回-1
    """

    for _, ele in enumerate(arr):
        if ele == target:
            return True

    return False


def main():
    """
    main执行函数
    """

    for _ in xrange(10):
        arr = sample(range(1, 11), 5)
        target = randint(1, 10)
        print arr, target, find(arr, target), target in arr
        assert find(arr, target) == (target in arr)


if __name__ == '__main__':
    main()
