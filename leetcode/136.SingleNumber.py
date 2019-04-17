#! /usr/bin/env python
# coding: utf-8

"""
题目： 唯一数字 https://leetcode-cn.com/problems/single-number/
主题： hash table & bit manipulation

解题思路：
1. 异或
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        
        for num in nums:
            result = result ^ num
            
        return result


if __name__ == '__main__':
    solution = Solution()
