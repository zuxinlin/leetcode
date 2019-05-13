#! /usr/bin/env python
# coding: utf-8

'''
题目： 最小路径和 https://leetcode-cn.com/problems/minimum-path-sum/
主题： dynamic programming

解题思路：
1. 状态转移方程：dp(i, j) = min(dp(i−1, j), dp(i, j−1)) + v(i, j)，表示在(i, j)这个点的路径和
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 降维解法
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n

        for i in range(0, m):
            for j in range(0, n):
                if i == 0:  # 向右走
                    dp[j] = dp[j-1]
                elif j == 0:  # 向下走
                    dp[j] = dp[j]
                else:
                    dp[j] = min(dp[j-1], dp[j])

                dp[j] += grid[i][j]

        return dp[n-1]

        # m = len(grid)
        # n = len(grid[0])
        # dp = [[0 for _ in range(n)] for _ in range(m) ]

        # for i in range(0, m):
        #     for j in range(0, n):
        #         if i == 0 and j == 0:
        #             dp[0][0] = grid[0][0]
        #         elif i == 0:
        #             dp[0][j] = dp[0][j-1] + grid[0][j]
        #         elif j == 0:
        #             dp[i][0] = dp[i-1][0] + grid[i][0]
        #         else:
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        # return dp[m-1][n-1]


if __name__ == '__main__':
    solution = Solution()
