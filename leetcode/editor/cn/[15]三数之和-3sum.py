#!/bin/env python
# coding: utf-8

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics 数组 双指针 
#  👍 3285 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []

        nums.sort()
        result = []

        for i, num in enumerate(nums[:-2]):
            if num > 0:  # 第一个数大于 0，后面的数都比它大，肯定不成立了
                break

            if i > 0 and nums[i] == nums[i - 1]:  # 去掉重复情况
                continue

            target = -num
            low, high = i + 1, len(nums) - 1

            while low < high:
                if nums[low] + nums[high] == target:
                    result.append([num, nums[low], nums[high]])
                    low += 1
                    high -= 1

                    # 避免重复
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1

                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif nums[low] + nums[high] > target:
                    high -= 1
                else:
                    low += 1

        return result


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    solution.threeSum([1, 1, 1])
