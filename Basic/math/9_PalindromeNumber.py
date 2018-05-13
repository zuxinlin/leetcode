#! /usr/bin/env python
# coding: utf-8
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

import sys
import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # 回文数，采用字符串反转的方式
        # if x < 0:
        #     return False
        # else:
        #     return str(x) == str(x)[::-1]

        # 另外一种方式就是看左边的数字是否等于右边的数字，分为奇数位和偶数位
        if x < 0 or x % 10 == 0:
            return False

        if x == 0:
            return True

        y = 0

        while y < x:
            y = y * 10 + x % 10
            x = x / 10

        return x == y or (y > x and y / 10 == x)


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPalindrome(-1) is False
    assert solution.isPalindrome(121) is True
