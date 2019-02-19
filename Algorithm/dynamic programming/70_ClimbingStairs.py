#! /usr/bin/env python
# coding: utf-8

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

给定楼层数n，每次可以爬1层或者2层，有几种爬法
状态转移方程：dp[i] = dp[i-1] + dp[i-2]，斐波那契数列
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return n

        result, first, second = 0, 1, 2

        for _ in range(3, n + 1):
            result = first + second
            first = second
            second = result

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
