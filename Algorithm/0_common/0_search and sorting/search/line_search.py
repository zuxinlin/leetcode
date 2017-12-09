#! /usr/bin/env python
# coding: utf - 8
"""
线性查找
"""


def find(arr, target):
    """
    给定一个数组和目标数，查找这个数是否在数组中，在的话返回下标，不在返回-1
    """

    for index, ele in enumerate(arr):
        if ele == target:
            return index

    return -1


def main():
    """
    main执行函数
    """

    arr = [1, 2, 3, 4]
    assert find(arr, 4) == 3
    assert find(arr, 5) == -1


if __name__ == '__main__':
    main()
    