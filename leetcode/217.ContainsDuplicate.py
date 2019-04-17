#! /usr/bin/env python
# coding: utf-8

'''
题目： 包含重复数字 https://leetcode-cn.com/problems/contains-duplicate/
主题： array & hash table

解题思路：
1. 哈希表
'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hash_table = set()
        
        for num in nums:
            if num in hash_table:
                return True
            else:
                hash_table.add(num)
                
        return False

if __name__ == '__main__':
    solution = Solution()
    