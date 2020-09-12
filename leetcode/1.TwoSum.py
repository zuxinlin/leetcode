#! /usr/bin/env python
# coding: utf-8

'''
题目： 两数之和 https://leetcode-cn.com/problems/two-sum/
主题： array & hash table

解题思路：
1. 直接对数组排序，然后分别从头（start）和从尾（end）向中间遍历，如果和大于目标值，end-1.如果和小于目标值，start+1，如果相等再去原数组找到相应的元素，这里有一个重复元素处理的问题。这是最笨的方法了，时间复杂度O(nlogn)O(nlog⁡n)（排序算法） 
2. 用一个字典来维护，key等于tar减num[i]的差值，value为i，这样从头到尾遍历一次，如果当前的值在字典的key中，直接去当前位置和字典中该key对应的value。时间复杂度O(n)
'''

class Solution(object):
    '''
    '''

    def twoPointer(self, nums, target):
        '''
        有序数组采用头尾双指针查找
        '''

        nums.sort()
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1

        return False

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 边界条件判断
        if len(nums) <= 1:
            return False

        # 以空间换时间，用字典存储，key是第二个加数，value是第一个加数的下标
        buff_dict = {}

        for i, first in enumerate(nums):
            if first in buff_dict:
                return [buff_dict[first], i]
            else:
                buff_dict[target - first] = i


if __name__ == '__main__':
    solution = Solution()
    # assert [0, 1] == solution.twoSum([2, 7, 11, 15], 9)
    assert [1, 2] == solution.twoSum([3, 2, 4], 6)
