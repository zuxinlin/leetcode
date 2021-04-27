#! /usr/bin/env python
# coding: utf-8

# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可
# 能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi" 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num < 231 
#  
#  👍 216 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return 1

        num = str(num)
        dp = [1] * len(num)
        dp[1] = 2 if '10' <= num <= '25' else 1

        for i in range(2, len(num)):
            if '10' <= num[i - 1:i + 1] <= '25':
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]

        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    print(solution.translateNum(12258))
