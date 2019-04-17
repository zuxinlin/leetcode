#! /usr/bin/env python
# coding: utf-8

import math

'''
题目： 因子尾0 https://leetcode-cn.com/problems/factorial-trailing-zeroes/
主题： math

解题思路：
1. 排序
'''


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0

        while n > 0:
            n = n // 5
            count += n
        return count


if __name__ == '__main__':
    solution = Solution()
    print solution.trailingZeroes(20)
