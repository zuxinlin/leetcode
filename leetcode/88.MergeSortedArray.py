#! /usr/bin/env python
# coding: utf-8

from itertools import combinations

'''
题目： 合并有序数组
主题： array & two pointers

解题思路：
1. 两个尾指针，比较大小
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        first_index = m - 1
        second_index = n - 1
        index = m + n - 1
        
        while first_index >= 0 and second_index >= 0:
            if nums1[first_index] >= nums2[second_index]:
                nums1[index] = nums1[first_index]
                first_index -= 1
            else:
                nums1[index] = nums2[second_index]
                second_index -= 1
                
            index -= 1
            
        while second_index >= 0:
            nums1[index] = nums2[second_index]
            index -= 1
            second_index -= 1

if __name__ == '__main__':
    solution = Solution()
