#! /usr/bin/env python
# coding: utf - 8

"""
快速排序
"""

from random import sample


def partition(arr, left, right):
    """
    默认把数组第一个元素认为是目标，把所有比他小的放在他前面，所有比他大的放在后面
    """

    target = arr[left]

    while left < right:
        if arr[right] >= target and left < right:
            right -= 1

        arr[left] = arr[right]

        if arr[left] <= target and left < right:
            left += 1

        arr[right] = arr[left]

    arr[left] = target

    return left


def quick_sort(arr, left, right):
    """
    快速排序(不稳定，时间复杂度nlgn)，分治法解决
    """
    if left < right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


def sort(arr):
    """
    快速排序
    """
    quick_sort(arr, 0, len(arr) - 1)

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
    print sort([2, 1, 1, 3])
