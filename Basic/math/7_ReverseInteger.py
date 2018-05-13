#! /usr/bin/env python
# coding: utf-8
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

import sys
import math


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2**31 - 1
        min_int = -1 * 2**31

        if x < 0:
            result = -1 * int(str(-x)[::-1])
        else:
            result = int(str(x)[::-1])

        if result > max_int or result < min_int:
            return 0
        else:
            return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(-120) == -21
