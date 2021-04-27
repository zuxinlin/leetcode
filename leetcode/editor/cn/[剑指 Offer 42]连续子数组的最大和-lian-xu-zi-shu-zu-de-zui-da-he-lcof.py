#! /usr/bin/env python
# coding: utf-8

# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。 
# 
#  要求时间复杂度为O(n)。 
# 
#  
# 
#  示例1: 
# 
#  输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  -100 <= arr[i] <= 100 
#  
# 
#  注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/ 
# 
#  
#  Related Topics 分治算法 动态规划 
#  👍 256 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        # 1. 确定状态
        # 3. 确定初始条件以及边界条件
        dp = [0] * len(nums)
        result = dp[0] = nums[0]

        for i in range(1, len(nums)):
            # 2. 找到转移公式
            dp[i] = nums[i] + max(dp[i - 1], 0)
            result = max(result, dp[i])

        return result

# if __name__ == '__main__':
#     solution = Solution()
#     assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

# leetcode submit region end(Prohibit modification and deletion)
