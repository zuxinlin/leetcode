#! /usr/bin/env python
# coding: utf-8

"""
题目： 唯一数字II https://leetcode-cn.com/problems/single-number-ii/
主题： bit manipulation

解题思路：
1. 排序
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # nums.sort()
        # length = len(nums)

        # for i in range(0, length - 2, 3):
        #     if nums[i] != nums[i + 2]:
        #         return nums[i]

        # return nums[-1]

        # 每个数字相应的位相加，然后模3，余数就是多的那个
        res = 0

        for i in range(32):
            count = 0
            
            for n in nums:
                count += (n >> i) & 1
                
            rem = count % 3
            
            if i == 31 and rem:  # must handle the negative case
                res -= 1 << 31
            else:
                res |= rem << i
        return res


if __name__ == '__main__':
    solution = Solution()
