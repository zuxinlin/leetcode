#! /usr/bin/env python
# coding: utf-8
"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Solution(object):
    """
    Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    For example,
    Given [3,2,1,5,6,4] and k = 2, return 5.

    Note: 
    You may assume k is always valid, 1 ≤ k ≤ array's length.
    """

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 排序，复杂度为n*lgn
        # return sorted(nums, reverse=True)[k-1]

        # 使用冒泡排序，复杂度为n*k
        for i in xrange(k):
            for j in xrange(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums[len(nums) - k]


if __name__ == '__main__':
    solution = Solution()
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
