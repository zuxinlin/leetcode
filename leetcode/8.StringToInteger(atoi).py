#! /usr/bin/env python
# coding: utf-8

'''
题目： 字符串转换整数 (atoi) https://leetcode-cn.com/problems/string-to-integer-atoi/
主题： string & math

解题思路：
1. 反转数字，注意判断正负数、是否越界，然后变成字符串反转
'''

import sys
import math


class Solution(object):
    '''
    '''

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # 边界条件
        str = str.strip()

        if not str:
            return 0

        max_int = 2147483647
        min_int = -2147483648
        is_negative = False
        result = 0
        index = 0

        # 判断正负数
        if str[0] == '-':
            is_negative = True
            index += 1
        elif str[0] == '+':
            index += 1

        for char in str[index:]:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        if is_negative:
            result = -1 * result

        if result > max_int:
            return max_int
        elif result < min_int:
            return min_int
        else:
            return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.myAtoi('42') == 42
    assert solution.myAtoi('   -42') == -42
    assert solution.myAtoi('4193 with words') == 4193
    assert solution.myAtoi('words and 987') == 0
    assert solution.myAtoi('-91283472332') == -2147483648
    assert solution.myAtoi('+1') == 1
    assert solution.myAtoi('+-2') == 0
