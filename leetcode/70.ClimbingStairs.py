#! /usr/bin/env python
# coding: utf-8

"""
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
