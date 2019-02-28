#! /usr/bin/env python
# coding: utf-8

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

最大抢劫数额，限制是不能抢相邻两家
状态转移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])，表示当前到i最大利润
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums is None or len(nums) < 1:
        #     return 0
        # elif len(nums) == 1:
        #     return nums[0]

        # dp = [0] * len(nums)
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        # return max(dp[-2], dp[-1])

        pre, cur = 0, 0

        for n in nums:
            pre, cur = cur, max(pre + n, cur)
        return cur


if __name__ == '__main__':
    solution = Solution()
    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([2, 7, 9, 3, 1]) == 12