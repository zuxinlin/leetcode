#! /usr/bin/env python
# coding: utf-8

'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

连续整数数组，其中丢失一个数字，求丢失的数字

1. 求和
2. 异或
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 加法求解
        # return (1 + len(nums)) * len(nums) / 2 - sum(nums)

        # 异或求解
        n = len(nums)
        first, second = 0, 0

        for i in range(n+1):
            first ^= i

        for i in nums:
            second ^= i

        return first^second


if __name__ == '__main__':
    solution = Solution()
    assert solution.missingNumber([3, 0, 1]) == 2
    assert solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
