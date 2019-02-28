#! /usr/bin/env python
# coding: utf - 8

"""
插入排序
"""

from random import sample


def sort(arr):
    """
    插入排序(稳定，时间复杂度n^2)，每次都插入到已经排好序的数组，调整位置
    """
    length = len(arr)

    for i in xrange(1, length):
        if arr[i] < arr[i - 1]:
            temp = arr[i]  # 当前需要排序的元素
            index = i  # 用来记录排序元素需要插入的位置

            while index > 0 and arr[index - 1] > temp:
                arr[index] = arr[index - 1]
                index -= 1

            arr[index] = temp

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
