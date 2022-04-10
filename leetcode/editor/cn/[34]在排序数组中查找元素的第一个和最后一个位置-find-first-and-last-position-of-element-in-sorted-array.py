#!/bin/env python
# coding: utf-8

# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  进阶： 
# 
#  
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  nums 是一个非递减数组 
#  -109 <= target <= 109 
#  
#  Related Topics 数组 二分查找 
#  👍 996 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 左界
        def left_bound():
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] >= target:  # 收缩右界
                    right = mid - 1
                else:
                    left = mid + 1

            if left >= len(nums) or nums[left] != target:
                return -1
            else:
                return left

        # 右界
        def right_bound():
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] <= target:  # 收缩左界
                    left = mid + 1
                else:
                    right = mid - 1

            if right < 0 or nums[right] != target:
                return -1
            else:
                return right

        l = left_bound()

        if l != -1:
            r = right_bound()

            return [l, r]
        else:
            return [-1, -1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
