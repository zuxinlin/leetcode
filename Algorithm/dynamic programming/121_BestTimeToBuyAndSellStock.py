#! /usr/bin/env python
# coding: utf-8

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

最好时机买卖股票
状态转移方程：dp[i] = max(dp[i-1], prices[i] - min)，表示当前到i最大利润
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
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
    assert solution.maxProfit([7,1,5,3,6,4]) == 5
    assert solution.maxProfit([7,6,4,3,1]) == 0
