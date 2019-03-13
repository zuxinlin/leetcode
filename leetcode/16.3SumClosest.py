#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    '''
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

    主题：array & two pointers
    题目：求数组三个数相加最接近target的组合

    解题思路：
    方法1：采用排序加双指针的方式来
    方法2：采用排序加哈希表的方式来，类似2sum，a + b + c = 0 => a = -b - c
    '''

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        min_sum = sum(nums[:3])  # 默认前三个元素和最接近

        for (i, num) in enumerate(nums):
            # 头尾双指针，遍历所有可能
            left, right = i + 1, len(nums) - 1

            while left < right:
                s = sum((num, nums[left], nums[right]))

                # 求出最近的和
                if abs(s - target) < abs(min_sum - target):
                    min_sum = s

                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return target

        return min_sum


if __name__ == '__main__':
    solution = Solution()
    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert solution.threeSumClosest([1, 1, 1, 0], -100) == 2
