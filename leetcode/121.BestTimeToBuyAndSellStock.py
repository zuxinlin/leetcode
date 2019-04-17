#! /usr/bin/env python
# coding: utf-8

'''
题目： 买卖股票的最佳时机 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
主题： array & dynamic programming

解题思路：
状态转移方程：dp[i] = max(dp[i-1], prices[i] - min)，表示当前到i最大利润
'''


class Solution(object):
    def maxProfit(self, prices):
        '''
        :type prices: List[int]
        :rtype: int
        '''

        # 边界条件
        if prices is None or len(prices) <= 1:
            return 0

        dp = [0 for _ in prices]
        min_price = prices[0]
        max_profit = 0

        for (i, price) in enumerate(prices[1:]):
            dp[i] = max(dp[i-1], price - min_price)
            min_price = min(price, min_price)
            max_profit = max(dp[i], max_profit)

        return max_profit


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
