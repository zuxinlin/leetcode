#! /usr/bin/env python
# coding: utf-8
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

二分查找法
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return left


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchInsert([1,3,5,6], 5) == 2
    assert solution.searchInsert([1,3,5,6], 2) == 1
    assert solution.searchInsert([1,3,5,6], 7) == 4
    assert solution.searchInsert([1,3,5,6], 0) == 0
