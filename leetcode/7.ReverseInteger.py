#! /usr/bin/env python
# coding: utf-8

import sys
import math

'''
题目： 整数反转 https://leetcode-cn.com/problems/reverse-integer/
主题： math

解题思路：
1. 反转数字，注意判断正负数、是否越界，然后变成字符串反转
'''


class Solution(object):
    '''
    '''

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
            # 超过整数表达范围
            return 0
        else:
            return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(-120) == -21
