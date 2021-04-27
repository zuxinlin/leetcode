#! /usr/bin/env python
# coding: utf-8

# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [3,4,3,3]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：nums = [9,1,7,9,7,9,7]
# 输出：1 
# 
#  
# 
#  限制： 
# 
#  
#  1 <= nums.length <= 10000 
#  1 <= nums[i] < 2^31 
#  
# 
#  
#  👍 170 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        result = None

        for num in nums:
            if num not in cache:
                cache[num] = 1
                result = num
            else:
                cache[num] += 1
                result = None

        for k in cache:
            if cache[k] == 1:
                return k
# leetcode submit region end(Prohibit modification and deletion)
