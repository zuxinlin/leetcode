
#! /usr/bin/env python
# coding: utf-8
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

二分查找法
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                left, right = middle, middle

                while left - 1 >= 0 and target == nums[left - 1]:
                    left -= 1

                while right + 1 < len(nums) and target == nums[right + 1]:
                    right += 1

                return [left, right]
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
