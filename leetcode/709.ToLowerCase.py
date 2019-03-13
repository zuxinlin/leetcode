#! /usr/bin/env python
# coding: utf-8

'''
题目： 转换成小写字母 https://leetcode-cn.com/problems/to-lower-case/
主题： string

解题思路：
1. 调用字符串库函数lower
'''


class Solution(object):
    '''
    '''

    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """

        # return str.lower()

        result = ''
        
        for c in str:
            if c >= 'A' and c <= 'Z':
                result += chr(ord(c) + 32)
            else:
                result += c
                
        return result


if __name__ == '__main__':
    solution = Solution()
    assert 'hello' == solution.toLowerCase('Hello')
