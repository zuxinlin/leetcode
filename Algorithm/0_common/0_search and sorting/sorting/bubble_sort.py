#! /usr/bin/env python
# coding: utf - 8
"""
冒泡排序
"""

from random import sample

def sort(arr):
    """
    冒泡排序，比较前后两个元素，如果前面比后面大，相互交换
    """
    l = len(arr)

    for i in xrange(l):
        for j in xrange(0, l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def main():
    for i in xrange(10):
        arr = sample(range(1, 10), 5)
        print arr,
        print sort(arr)
        assert sort(arr) == sorted(arr)

if __name__ == '__main__':
    main()