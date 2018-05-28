#! /usr/bin/env python
# coding: utf - 8
"""
冒泡排序
"""

from random import sample


def sort(arr):
    """
    冒泡排序(稳定，时间复杂度n^2)，比较前后两个元素，如果前面比后面大，相互交换
    """
    length = len(arr)

    for i in xrange(length):
        for j in xrange(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def main():
    """
    main执行函数
    """
    for _ in xrange(10):
        arr = sample(range(1, 10), 5)
        print arr, sort(arr)
        assert sort(arr) == sorted(arr)


if __name__ == '__main__':
    main()
