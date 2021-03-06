#! /usr/bin/env python
# coding: utf-8

'''
题目：
主题：

解题思路：
1. 状态转移方程：dp[i] = dp[i-1] + dp[i-2]，斐波那契数列
'''


class Solution(object):
    def climbStairs(self, n):
        '''
        :type n: int
        :rtype: int
        '''

        if n <= 2:
            return n

        first, second = 1, 2

        for _ in range(3, n + 1):
            second, first = first + second, second

        return second


if __name__ == '__main__':
    solution = Solution()
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
