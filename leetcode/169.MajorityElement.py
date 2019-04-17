#! /usr/bin/env python
# coding: utf-8

'''
题目： 主要元素 https://leetcode-cn.com/problems/majority-element/
主题： array & divide and conquer & bit manipulation

解题思路：
1. 排序
'''


class Solution(object):
    def majorityElement(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        # return sorted(num)[len(num)/2]

        # 用字典存储每个元素出现次数，并且记录当前出现最多的元素以及个数
        d = {}
        count = 0
        target = 0

        for i in nums:
            d[i] = d[i] + 1 if d.has_key(i) else 1

            if d[i] > count:
                target = i
                count = d[i]

        return target


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 3, 4]
    assert 2 == solution.majorityElement(nums)
