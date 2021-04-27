#! /usr/bin/env python
# coding: utf-8

# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,5,6,4]
# 输出: 5 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 50000 
#  👍 399 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def merge_sort(l, r):
            # 终止条件
            if l >= r:
                return 0

            # 递归划分
            m = l + (r - l) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)

            # 合并
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]

            for k in range(l, r + 1):
                if i == m + 1:  # 左边线结束，一直拷贝右侧子数组
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:  # 右边先结束
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1  # 统计逆序对

            return res

        tmp = [0] * len(nums)

        return merge_sort(0, len(nums) - 1)
# leetcode submit region end(Prohibit modification and deletion)
