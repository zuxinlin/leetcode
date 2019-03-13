#! /usr/bin/env python
# coding: utf-8

'''
题目： 罗马数字转整数 https://leetcode-cn.com/problems/roman-to-integer/
主题： math & string

解题思路：
1. hash表存储字符代表的值，遍历字符串，如果前面字符串值比后面小，就减掉，其他加上；
'''

import sys
import math


class Solution(object):
    '''
    '''

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sum = 0

        for (index, element) in enumerate(s):
            if index < len(s) - 1 and cache[element] < cache[s[index + 1]]:
                sum -= cache[element]
            else:
                sum += cache[element]

        return sum


if __name__ == '__main__':
    solution = Solution()
    assert solution.romanToInt('III') == 3
    assert solution.romanToInt('IV') == 4
    assert solution.romanToInt('IX') == 9
    assert solution.romanToInt('LVIII') == 58
    assert solution.romanToInt('MCMXCIV') == 1994
