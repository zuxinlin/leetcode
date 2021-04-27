#! /usr/bin/env python
# coding: utf-8

# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2] 
# 
#  
# 
#  限制： 
# 
#  
#  2 <= nums.length <= 10000 
#  
# 
#  
#  👍 373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret, h, a, b = 0, 1, 0, 0

        # 全部以后得到a^b
        for num in nums:
            ret ^= num

        # 找到a b第一个差别的位；可以把a和b分为两组
        while ret & h == 0:
            h <<= 1

        for num in nums:
            if num & h == 0:
                a ^= num
            else:
                b ^= num

        return [a, b]

# leetcode submit region end(Prohibit modification and deletion)
