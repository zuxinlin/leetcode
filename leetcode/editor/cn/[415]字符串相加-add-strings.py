#!/bin/env python
# coding: utf-8

# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。 
# 
#  
# 
#  提示： 
# 
#  
#  num1 和num2 的长度都小于 5100 
#  num1 和num2 都只包含数字 0-9 
#  num1 和num2 都不包含任何前导零 
#  你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式 
#  
#  Related Topics 字符串 
#  👍 360 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
