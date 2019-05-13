#! /usr/bin/env python
# coding: utf-8

'''
题目： 不同路径 https://leetcode-cn.com/problems/unique-paths/
主题： dynamic programming

解题思路：
1. 状态转移方程：dp(i, j)=dp(i−1, j) + dp(i, j−1)，表示在(i, j)这个点的方法数
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 降为写法
        # dp = [0] * n

        # for i in range(0, m):
        #     for j in range(0, n):
        #         if i == 0 or j == 0: # 只能向下或者向右走，一种方式
        #             dp[j] = 1
        #         else:
        #             dp[j] += dp[j-1]

        # return dp[n-1]

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:  # 往右或者往下走，只有一种方式
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


if __name__ == '__main__':
    solution = Solution()
