#! /usr/bin/env python
# coding: utf-8

"""
Given an array of integers, return indices of the two numbers such that they add
up to a specific target. You may assume that each input would have exactly one
solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

主题：array & hash table
题目：求数组内两个数字相加和为一个目标数的下标
方法1：采用哈希表存储，key是第一个加数，value是第二个加数的下标
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 边界条件判断
        if len(nums) <= 1:
            return False

        # 以空间换时间，用字典存储，key是第二个加数，value是第一个加数的下标
        buff_dict, l = {}, len(nums)

        for i in range(l):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


if __name__ == '__main__':
    solution = Solution()
    # assert [0, 1] == solution.twoSum([2, 7, 11, 15], 9)
    assert [1, 2] == solution.twoSum([3, 2, 4], 6)
