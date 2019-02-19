#! /usr/bin/env python
# coding: utf - 8
"""
二分查找
"""


def find(arr, target):
    """
    给定一个有序数组和目标数，查找这个数是否在数组中，在的话返回下标，不在返回-1
    """

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) / 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def recursive_find(arr, target, l, r):
    """
    给定一个有序数组和目标数，查找这个数是否在数组中，在的话返回下标，不在返回-1
    """

    if l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recursive_find(arr, target, l + 1, r)
        else:
            return recursive_find(arr, target, l, r - 1)
    else:
        return -1


def main():
    """
    main执行函数
    """

    arr = [1, 2, 3, 4]
    assert find(arr, 4) == 3
    assert find(arr, 5) == -1
    assert recursive_find(arr, 4, 0, len(arr) - 1) == 3
    assert recursive_find(arr, 5, 0, len(arr) - 1) == -1


if __name__ == '__main__':
    main()
