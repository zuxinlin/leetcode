#! /usr/bin/env python
# coding: utf-8

'''
题目： 正则表达式匹配 https://leetcode-cn.com/problems/regular-expression-matching/
主题： string & dynamic programming & backtracking

解题思路：
1. 动态规划，dp[i][j] == True 表示p的前面j个字符可以匹配s的前面i个字符。初始化需要考虑p和s为空的情况。
p为空，都是False。
'''

import re
import math


class Solution(object):
    '''
    '''

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # 初始化
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[0][0] = True

        for j in range(2, len_p + 1):
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'

        # 遍历
        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] in ('.', s[i-1]))
                else:
                    dp[i][j] = dp[i-1][j-1] and p[j-1] in ('.', s[i-1])

        return dp[len_s][len_p]


if __name__ == '__main__':
    solution = Solution()
    assert solution.isMatch('aa', 'a') is False
    assert solution.isMatch('', 'a*') is True
