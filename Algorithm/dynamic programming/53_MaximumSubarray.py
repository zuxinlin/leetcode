#! /usr/bin/env python
# coding: utf-8

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

最大连续子数组和
状态转移方程：dp[i] = nums[i] + dp[i - 1] if dp[i - 1] > 0 else 0，表示当前到i最大子数组和
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # dp[i] means the maximum subarray ending with A[i]
        # l = len(nums)
        # dp = [0] * l
        # dp[0] = nums[0]
        # result = dp[0]
        # for i in xrange(1, l):
        #     add = dp[i - 1] if dp[i - 1] > 0 else 0
        #     dp[i] = nums[i] + add
        #     result = max(result, dp[i])
        # return result

        # 默认第一个元素构成的子数组最大，如果在加入一个元素，如果前面的元素大于0，则加入，否则不加入
        current, result = nums[0], nums[0]

        for ele in nums[1:]:
            current = ele + (current if current > 0 else 0)
            result = max(result, current)

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
