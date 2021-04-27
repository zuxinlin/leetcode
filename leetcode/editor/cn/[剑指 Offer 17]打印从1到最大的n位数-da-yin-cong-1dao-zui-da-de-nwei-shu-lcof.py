#! /usr/bin/env python
# coding: utf-8

# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。 
# 
#  示例 1: 
# 
#  输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
#  
# 
#  
# 
#  说明： 
# 
#  
#  用返回一个整数列表来代替打印 
#  n 为正整数 
#  
#  Related Topics 数学 
#  👍 111 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        count = 1

        for i in range(n):
            count *= 10

        return [i for i in range(1, count)]
# leetcode submit region end(Prohibit modification and deletion)
