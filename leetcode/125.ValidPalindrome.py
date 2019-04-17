#! /usr/bin/env python
# coding: utf-8

'''
题目： 合法回文串 https://leetcode-cn.com/problems/valid-palindrome/
主题： two pointers & array

解题思路：
忽略头尾不是数字字母的字符，然后比较
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


if __name__ == '__main__':
    solution = Solution()
