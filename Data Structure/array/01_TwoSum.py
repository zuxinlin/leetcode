#! /usr/bin/env python
# coding: utf-8
"""
Two Sum
"""


class Solution(object):
    """
    Given an array of integers, return indices of the two numbers such that they add
    up to a specific target. You may assume that each input would have exactly one
    solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """

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
    nums = [2, 7, 11, 15]
    target = 9
    assert [0, 1] == solution.twoSum(nums, target)
