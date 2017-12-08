#! /usr/bin/env python
# coding: utf-8
"""
Majority Element
"""


class Solution(object):
    """
    Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always exist in the array.
    """

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

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
