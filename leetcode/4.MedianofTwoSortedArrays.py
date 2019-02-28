#! /usr/bin/env python
# coding: utf-8

'''
题目： 寻找两个有序数组的中位数 https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
主题： array & binary search & divide and conquer

解题思路：
1. 两个数组合并，然后判断合并后的数组是奇数个还是偶数个
'''


class Solution(object):
    '''
    '''

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # 两个数组合并然后排序，然后看数组大小是奇数还是偶数
        # 奇数的话就是中间的那个，偶数中间两个求平均数
        nums = nums1 + nums2
        nums.sort()
        m = len(nums) / 2
        mm = len(nums) % 2

        if mm > 0:
            return nums[m]
        else:
            return (nums[m - 1] + nums[m]) / 2.0


if __name__ == '__main__':
    solution = Solution()
    nums1 = [2, 1, 6]
    nums2 = [4, 3, 5]
    assert 3.5 == solution.findMedianSortedArrays(nums1, nums2)
