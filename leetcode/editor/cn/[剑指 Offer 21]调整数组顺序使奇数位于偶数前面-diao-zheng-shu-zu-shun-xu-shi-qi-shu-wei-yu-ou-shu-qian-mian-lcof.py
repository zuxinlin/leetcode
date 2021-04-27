#! /usr/bin/env python
# coding: utf-8

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 50000 
#  1 <= nums[i] <= 10000 
#  
#  👍 116 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        i, j = 0, len(nums) - 1

        for num in nums:
            if num & 1 == 1:
                result[i] = num
                i += 1
            else:
                result[j] = num
                j -= 1

        return result


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
