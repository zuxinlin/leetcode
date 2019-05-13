#! /usr/bin/env python
# coding: utf-8

'''
二分查找
'''


def binary_search(arr, target):
    '''
    给定一个有序数组和目标数，查找这个数是否在数组中，在的话返回下标，不在返回-1
    '''

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) / 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_position(arr, target):
    '''
    给定一个有序重复数组和目标数，查找这个数是否在数组中，在的话返回下标，不在返回-1
    '''

    left, right = 0, len(arr) - 1

    while left < right: # 保证可以退出循环
        mid = left + (right - left) / 2

        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left if arr[left] == target else -1


def recursive_binary_search(arr, target, l, r):
    '''
    给定一个有序数组和目标数，查找这个数是否在数组中，在的话返回下标，不在返回-1
    '''

    if l <= r:
        mid = l + (r - l) / 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recursive_binary_search(arr, target, l + 1, r)
        else:
            return recursive_binary_search(arr, target, l, r - 1)
    else:
        return -1


def main():
    '''
    main执行函数
    '''

    arr = [1, 2, 3, 4, 4, 4, 8, 10, 12]
    print binary_search_position(arr, 4)
    print binary_search(arr, 16)
    print recursive_binary_search(arr, 4, 0, len(arr) - 1)
    print recursive_binary_search(arr, 5, 0, len(arr) - 1) 
    print binary_search_position([1, 2, 2, 2, 3], 5)


if __name__ == '__main__':
    main()
