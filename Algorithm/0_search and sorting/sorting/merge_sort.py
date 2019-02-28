#! /usr/bin/env python
# coding: utf - 8

"""
归并排序 - 分治法
"""

from random import sample


def merge(first, second):
    """
    合并两个有序数组，先从头遍历两个数组小的元素，遍历完一个数组后，把另外一个全插入新数组
    """

    i = j = 0
    third = []

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            third.append(first[i])
            i += 1
        else:
            third.append(second[j])
            j += 1

    if i == len(first):
        for data in second[j:]:
            third.append(data)
    else:
        for data in first[i:]:
            third.append(data)

    return third


def sort(arr):
    """
    归并排序(稳定，时间复杂度nlgn，空间复杂度n)，分治法解决；
    把数组拆成两个数组，分别排序，然后合并起来
    """
    if len(arr) <= 1:
        return arr

    middle = len(arr) / 2
    left = sort(arr[:middle])
    right = sort(arr[middle:])

    return merge(left, right)


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
