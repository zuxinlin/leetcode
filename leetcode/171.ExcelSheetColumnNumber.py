#! /usr/bin/env python
# coding: utf-8

'''
题目： 主要元素 https://leetcode-cn.com/problems/excel-sheet-column-number/
主题： math

解题思路：
1. 排序
'''


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        start = ord('A') - 1
        
        for c in s:
            result = result * 26 + (ord(c) - start)
            
        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.titleToNumber('A')
    print solution.titleToNumber('AB')
    print solution.titleToNumber('ZY')
    
