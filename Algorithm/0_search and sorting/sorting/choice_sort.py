#! /usr/bin/env python
# coding: utf - 8

"""
选择排序
"""

from random import sample


def sort(arr):
    """
    选择排序(不稳定，时间复杂度n^2)，每次选择剩下里面最小的放在带排序的位置
    """
    length = len(arr)

    for i in xrange(0, length - 1):
        # 默认当前元素是最小的
        index = i

        for j in xrange(i + 1, length):
            # 如果有更小的元素，更新下标
            if arr[j] < arr[index]:
                index = j

        if i != index:
            arr[i], arr[index] = arr[index], arr[i]

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
