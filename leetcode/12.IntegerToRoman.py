#! /usr/bin/env python
# coding: utf-8

'''
题目： 整数转罗马数字 https://leetcode-cn.com/problems/integer-to-roman/
主题： math & string

解题思路：
1. 把数字转成有几个千，几个百，几个十；
'''


class Solution(object):
    '''
    '''

    def intToRoman(self, num):
        '''
        :type num: int
        :rtype: str
        '''

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC",
                    "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        
        for i, v in enumerate(values):
            res += (num//v) * numerals[i]
            num %= v
        return res


if __name__ == '__main__':
    pass
