#! /usr/bin/env python
# coding: utf-8

# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。 
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2： 
# 
#  
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= word1.length, word2.length <= 500 
#  word1 和 word2 由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 1560 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        row, column = len(word1), len(word2)
        dp = [list(0 for _ in range(column + 1)) for _ in range(row + 1)]

        # 初始化状态
        for i in range(1, row + 1):
            dp[i][0] = i

        for i in range(1, column + 1):
            dp[0][i] = i

        for i in range(1, row + 1):
            for j in range(1, column + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1],
                                   dp[i - 1][j]) + 1

        return dp[row][column]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance('', 'a'))
# leetcode submit region end(Prohibit modification and deletion)
