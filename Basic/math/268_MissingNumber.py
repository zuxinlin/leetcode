#! /usr/bin/env python
# coding: utf-8
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""

import sys
import math


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return (1 + len(nums)) * len(nums) / 2 - sum(nums)


if __name__ == '__main__':
    solution = Solution()
    assert solution.missingNumber([1, 2, 4]) == 3
    
