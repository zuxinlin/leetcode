#! /usr/bin/env python
# coding: utf-8

"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

最小代价爬到楼顶，每次可以走一步或者两步
状态转移方程：dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])，表示到达第i层最小的代价
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2]+cost[i], dp[i-1]+cost[i])

        return min(dp[-2], dp[-1])


if __name__ == '__main__':
    solution = Solution()
    assert solution.minCostClimbingStairs([10, 15, 20]) == 15
    assert solution.minCostClimbingStairs(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
