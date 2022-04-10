#!/bin/env python
# coding: utf-8

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 1048 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 冒泡排序
        # n = len(nums)
        # for i in range(n):
        #     for j in range(0, n - i - 1):
        #         if nums[j] == 0:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # 双指针
        # 左指针左边均为非零数；右指针左边直到左指针处均为零。

        n = len(nums)
        left = right = 0

        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

            right += 1



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    solution.moveZeroes([0, 0, 1])
