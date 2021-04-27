#! /usr/bin/env python
# coding: utf-8

# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。 
# 
#  
# 
#  你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 1
# 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
#  
# 
#  示例 2: 
# 
#  输入: 2
# 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0
# .05556,0.02778] 
# 
#  
# 
#  限制： 
# 
#  1 <= n <= 11 
#  👍 218 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """

        """
有i个骰子，掷出和为j的可能性 == (有1个骰子，掷出和为1~6的可能性) *= (有i-1个骰子，掷出和为j-(1~6)的可能性)
根据推导，我们能够知道：
dp[i][j] += dp[1][k] * dp[i - 1][j - k];
k为 合理情况下 的 1～6
"""
        base = 1.0 / 6
        dp = [[0] * (6 * _ + 1) for _ in range(n + 1)]

        for k in range(1, 7):
            dp[1][k] = base

        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                dp[i][j] = sum(dp[i - 1][max(0, j - 6):j]) * base

        return dp[n][n:]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
