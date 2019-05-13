#! /usr/bin/env python
# coding: utf - 8

'''
排序算法
'''

from random import sample


def choice_sort(arr):
    '''
    选择排序(不稳定，时间复杂度n^2)，每次选择剩下里面最小的放在带排序的位置
    '''
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


def bubble_sort(arr):
    '''
    冒泡排序(稳定，时间复杂度n^2)，比较前后两个元素，如果前面比后面大，相互交换
    '''
    length = len(arr)

    for i in xrange(length):
        for j in xrange(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insert_sort(arr):
    '''
    插入排序(稳定，时间复杂度n^2)，每次都插入到已经排好序的数组，调整位置
    '''
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


def quick_sort(arr):
    '''
    快速排序(不稳定，时间复杂度nlogn)，分治法解决
    '''
    def sort(arr, left, right):
        def partition(arr, left, right):
            '''
            默认把数组第一个元素认为是目标，把所有比他小的放在他前面，所有比他大的放在后面
            '''

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

        if left < right:
            mid = partition(arr, left, right)
            sort(arr, left, mid - 1)
            sort(arr, mid + 1, right)

    sort(arr, 0, len(arr) - 1)

    return arr


def merge_sort(arr):
    '''
    归并排序(稳定，时间复杂度nlogn，空间复杂度n)，分治法解决；
    把数组拆成两个数组，分别排序，然后合并起来
    '''
    if len(arr) <= 1:
        return arr

    def merge(first, second):
        '''
        合并两个有序数组，先从头遍历两个数组小的元素，遍历完一个数组后，把另外一个全插入新数组
        '''

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

    middle = len(arr) / 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def main():
    '''
    main执行函数
    '''
    for _ in xrange(10):
        arr = sample(range(1, 10), 5)
        assert choice_sort(arr) == sorted(arr)

    for _ in xrange(10):
        arr = sample(range(1, 10), 5)
        assert bubble_sort(arr) == sorted(arr)

    for _ in xrange(10):
        arr = sample(range(1, 10), 5)
        assert insert_sort(arr) == sorted(arr)

    for _ in xrange(10):
        arr = sample(range(1, 10), 5)
        assert quick_sort(arr) == sorted(arr)

    for _ in xrange(10):
        arr = sample(range(1, 10), 5)
        assert merge_sort(arr) == sorted(arr)


if __name__ == '__main__':
    # main()
    print reduce(lambda x, y: x * y, range(1, 6))
    print reduce(lambda x, y: x + y, range(1, 6))
    print filter(lambda x: x & 1 == 1, range(1, 5))
