#! /usr/bin/env python
# coding: utf-8

'''
题目： 编辑距离 https://leetcode-cn.com/problems/edit-distance/
主题： string & dynamic programming

解题思路：
1. 状态转移方程：dp(i, j) = dp(i-1, j-1) if s1[i]==s2[j] else min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
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
