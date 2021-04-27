#! /usr/bin/env python
# coding: utf-8

# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#  
# 
#  示例 2： 
# 
#  
# 输入：x = 2.10000, n = 3
# 输出：9.26100 
# 
#  示例 3： 
# 
#  
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25 
# 
#  
# 
#  提示： 
# 
#  
#  -100.0 < x < 100.0 
#  -231 <= n <= 231-1 
#  -104 <= xn <= 104 
#  
# 
#  
# 
#  注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/ 
#  Related Topics 递归 
#  👍 147 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 分治思想
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1.0 / x, -n)
        elif n & 1:
            return self.myPow(x, n - 1) * x
        else:
            return self.myPow(x * x, n / 2)


if __name__ == '__main__':
    solution = Solution()
    solution.myPow(2.00000, -2)
# leetcode submit region end(Prohibit modification and deletion)
