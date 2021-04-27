#! /usr/bin/env python
# coding: utf-8

# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nu
# ms2 的元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m + n 
#  nums2.length == n 
#  0 <= m, n <= 200 
#  1 <= m + n <= 200 
#  -109 <= nums1[i], nums2[i] <= 109 
#  
#  Related Topics 数组 双指针 
#  👍 931 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # 排序
        # nums1[m:] = nums2
        # nums1.sort()

        # 双指针 + 开辟新空间
        # result = []
        # p1, p2 = 0, 0
        #
        # while p1 < m or p2 < n:
        #     if p1 == m:
        #         result.append(nums2[p2])
        #         p2 += 1
        #     elif p2 == n:
        #         result.append(nums1[p1])
        #         p1 += 1
        #     elif nums1[p1] <= nums2[p2]:
        #         result.append(nums1[p1])
        #         p1 += 1
        #     elif nums1[p1] > nums2[p2]:
        #         result.append(nums2[p2])
        #         p2 += 1
        #
        # nums1[:] = result

        # 逆向双指针
        p1, p2, tail = m - 1, n - 1, m + n - 1

        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1

            tail -= 1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
