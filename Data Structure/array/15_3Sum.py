#! /usr/bin/env python
# coding: utf-8

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

主题：array & two pointer(二分法)
题目：求数组三个数相加等于0的所有可能组合
方法1：采用排序加二分的方式来
方法2：采用排序加哈希表的方式来，类似2sum
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 边界条件判断
        # if len(nums) <= 2:
        #     return []

        # nums.sort()
        # result = []

        # for (i, num) in enumerate(nums):
        #     if i > 0 and num == nums[i-1]:
        #         continue

        #     left, right = i + 1, len(nums) - 1

        #     while left < right:
        #         sum = num + nums[left] + nums[right]
        #         if sum == 0:
        #             result.append([num, nums[left], nums[right]])

        #             # 排除相同的数字组合
        #             left += 1
        #             right -= 1
        #             while nums[left] == nums[left - 1] and nums[right] == nums[right + 1] and left < right:
        #                 left += 1
        #         elif sum > 0:
        #             right -= 1
        #             while left < right and nums[right+1] == nums[right]:
        #                 right -= 1
        #         else:
        #             left += 1
        #             while left < right and nums[left-1] == nums[left]:
        #                 left += 1

        # return result

        if len(nums) < 3:
            return []

        nums.sort()
        res = set()

        for i, v in enumerate(nums[:-2]):
            # 相同的值，直接过掉，避免重复
            if i >= 1 and v == nums[i - 1]:
                continue

            d = {}

            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))

        return map(list, res)


if __name__ == '__main__':
    solution = Solution()
    print solution.threeSum([-1, 0, 1, 2, -1, -4])
