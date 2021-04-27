#! /usr/bin/env python
# coding: utf - 8

"""
排序算法
"""

from random import sample, randint


def choice_sort(arr):
    """
    选择排序(不稳定，时间复杂度n^2)，每次选择剩下里面最小的放在带排序的位置
    """
    length = len(arr)

    for i in range(0, length - 1):
        # 默认当前元素是最小的
        index = i

        for j in range(i + 1, length):
            # 如果有更小的元素，更新下标
            if arr[j] < arr[index]:
                index = j

        if i != index:
            arr[i], arr[index] = arr[index], arr[i]

    return arr


def bubble_sort(arr):
    """
    冒泡排序(稳定，时间复杂度n^2)，比较前后两个元素，如果前面比后面大，相互交换
    """
    length = len(arr)

    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insert_sort(arr):
    """
    插入排序(稳定，时间复杂度n^2)，每次都插入到已经排好序的数组，调整位置
    """
    length = len(arr)

    for i in range(1, length):
        if arr[i] < arr[i - 1]:
            temp = arr[i]  # 当前需要排序的元素
            index = i  # 用来记录排序元素需要插入的位置

            while index > 0 and arr[index - 1] > temp:
                arr[index] = arr[index - 1]
                index -= 1

            arr[index] = temp

    return arr


def quick_sort(arr, low, high):
    """
    快速排序(不稳定，时间复杂度nlogn)，分治法解决
    """

    def partition(arr, l, r):
        # 随机生成
        pivot = randint(l, r)
        # 将pivot和最后的元素交换，这样比较的时候不会和pivot相比较，同时也让最后一个元素参与了比较
        arr[pivot], arr[r] = arr[r], arr[pivot]
        # i左边都比pivot小
        i = l - 1

        for j in range(l, r):
            if arr[j] < arr[r]:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]

        i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

    return arr


def merge_sort(arr, low, high):
    """
    归并排序(稳定，时间复杂度nlogn，空间复杂度n)，分治法解决；
    把数组拆成两个数组，分别排序，然后合并起来
    """

    def merge(arr, low, mid, high):
        """
        合并两个有序数组，先从头遍历两个数组小的元素，遍历完一个数组后，把另外一个全插入新数组
        """

        tmp = []
        i, j = low, mid + 1

        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1

        while i <= mid:
            tmp.append(arr[i])
            i += 1

        while j <= high:
            tmp.append(arr[j])
            j += 1

        for i in range(len(tmp)):
            arr[low + i] = tmp[i]

    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

    return arr


def main():
    """
    main执行函数
    """
    # for _ in range(10):
    #     arr = sample(range(1, 10), 5)
    #     assert choice_sort(arr) == sorted(arr)
    #
    # for _ in range(10):
    #     arr = sample(range(1, 10), 5)
    #     assert bubble_sort(arr) == sorted(arr)
    #
    # for _ in range(10):
    #     arr = sample(range(1, 10), 5)
    #     assert insert_sort(arr) == sorted(arr)

    for _ in range(1000):
        arr = sample(range(0, 100), 100)
        assert quick_sort(arr, 0, len(arr) - 1) == sorted(arr)

    # for _ in range(1000):
    #     arr = sample(range(0, 100), 100)
    #     assert merge_sort(arr, 0, len(arr) - 1) == sorted(arr)


if __name__ == '__main__':
    main()
