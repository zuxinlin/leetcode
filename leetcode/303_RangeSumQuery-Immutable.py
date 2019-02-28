#! /usr/bin/env python
# coding: utf-8

"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

最大抢劫数额，限制是不能抢相邻两家
状态转移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])，表示当前到i最大利润
"""


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = {-1:0}

        for i,num in enumerate(nums):
            self.sum[i] = self.sum[i-1] + num

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        return self.sum[j] - self.sum[i-1]


if __name__ == '__main__':
    solution = Solution([-2, 0, 3, -5, 2, -1])
    assert solution.sumRange(0, 2) == 1
    assert solution.sumRange(2, 5) == -1
    assert solution.sumRange(0, 5) == -3
