#! /usr/bin/env python
# coding: utf-8

"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

求一个数是否是3的幂次方
"""

import sys
import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return n > 0 and 1162261467 % n == 0

        # 递归写法
        # if n == 0:
        #     return False
        # elif n == 1:
        #     return True
        # elif n % 3:
        #     return False

        # return self.isPowerOfThree(n / 3)

        if n == 0:
            return False

        while n % 3 == 0:
            n = n / 3

        return n == 1


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPowerOfThree(3)
