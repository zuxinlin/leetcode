#! /usr/bin/env python
# coding: utf-8

import sys

'''
题目：画家分区问题 https://practice.geeksforgeeks.org/problems/the-painters-partition-problem/0
主题：binary search & divide and conquer & dynamic programming & searching
公司：google

解题思路：
先把数字字母找出来，然后从前面往中间遍历，只要不是一样，直接打印no
'''


def sum(arr, frm, to):
    total = 0

    for i in range(frm, to):
        total += arr[i]

    return total


def partition(arr, n, k):
    '''
    for n boards and k partitions
    '''

    # base cases
    if k == 1:  # one partition
        return sum(arr, 0, n)
    elif n == 1:  # one board
        return arr[0]
    else:
        best = 100000000

        # find minimum of all possible
        # maximum k-1 partitions to
        # the left of arr[i], with i
        # elements, put k-1 th divider
        # between arr[i-1] & arr[i] to
        # get k-th partition
        for i in range(1, n + 1):
            best = min(best,
                       max(partition(arr, i, k - 1),
                           sum(arr, i, n)))
        return best


def find_max(arr, n, k):
    # dp[k][n]表示k个画家，n个木板需要最少的时间
    dp = [[0, ]*(n + 1) for _ in range(k+1)]
    s = [0] * (n + 1)

    # 事先算好0到i木板的和
    for i in range(1, n + 1):
        s[i] = s[i - 1] + arr[i - 1]

    # 一个木板
    for i in range(1, k+1):
        dp[i][1] = arr[0]

    # 一个画家
    for i in range(1, n + 1):
        dp[1][i] = s[i]

    for i in range(2, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = 9999999999

            for p in range(1, j):
                dp[i][j] = min(dp[i][j], max(dp[i-1][p], s[j] - s[p]))

    return dp[k][n]


if __name__ == "__main__":
    count = int(input())

    for _ in range(count):
        k, n = list(map(lambda x: int(x), input().split()))
        boards = list(map(lambda x: int(x), input().split()))

        print(find_max(boards, n, k))
