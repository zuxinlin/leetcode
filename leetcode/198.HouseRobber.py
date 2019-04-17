#! /usr/bin/env python
# coding: utf-8

'''
题目：
主题：

解题思路：
最大抢劫数额，限制是不能抢相邻两家
状态转移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])，表示当前到i最大利润
'''


class Solution(object):
    def rob(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
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
