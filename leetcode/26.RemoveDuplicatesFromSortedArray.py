#! /usr/bin/env python
# coding: utf-8

'''
题目： 从排序数组中删除重复项
主题：array & hash table & two pointers

解题思路：
1. 要求利用O(1)的空间，不得另辟空间。利用一个变量计数，只有不重复的时候才统计
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums is None or len(nums) == 0:
            return 0

        i = 1

        for n in nums[1:]:
            # 只有不重复的数字，才统计
            if n > nums[i - 1]:
                nums[i] = n
                i += 1

        return i


if __name__ == '__main__':
    solution = Solution()
    assert solution.removeDuplicates([1, 1, 2]) == 2
    assert solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
