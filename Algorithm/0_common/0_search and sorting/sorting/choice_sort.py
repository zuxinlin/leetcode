#! /usr/bin/env python
# coding: utf - 8
"""
选择排序
"""

from random import sample

def sort(arr):
    """
    选择排序，每次选择剩下里面最小的放在带排序的位置
    """
    l = len(arr)

    for i in xrange(0, l - 1):
        # 默认当前元素是最小的
        index = i

        for j in xrange(i + 1, l):
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

    # sort([6, 8, 5, 3, 1])
    for i in xrange(10):
        arr = sample(range(1, 10), 5)
        print arr,
        print sort(arr)
        assert sort(arr) == sorted(arr)

if __name__ == '__main__':
    main()
