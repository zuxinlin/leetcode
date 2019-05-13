#! /usr/bin/env python
# coding: utf-8

'''
题目： 不同路径2 https://leetcode-cn.com/problems/unique-paths-ii/
主题： dynamic programming

解题思路：
1. 状态转移方程：dp(i, j)=dp(i−1, j) + dp(i, j−1)，表示在(i, j)这个点的方法数
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not obstacleGrid:
            return

        # 降为写法
        # r, c = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [0] * c
        # dp[0] = 1 - obstacleGrid[0][0]

        # for i in xrange(1, c):
        #     dp[i] = dp[i-1] * (1 - obstacleGrid[0][i])

        # for i in xrange(1, r):
        #     dp[0] *= (1 - obstacleGrid[i][0])
        #     for j in xrange(1, c):
        #         dp[j] = (dp[j-1] + dp[j]) * (1 - obstacleGrid[i][j])

        # return dp[-1]

        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]

        for i in xrange(1, r):  # 往下走
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])

        for i in xrange(1, c):  # 往右走
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])

        for i in xrange(1, r):
            for j in xrange(1, c):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
