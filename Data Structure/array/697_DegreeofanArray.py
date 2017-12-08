#! /usr/bin/env python
# coding: utf-8
"""
Degree of an Array
"""
import collections


class Solution(object):
    """
    Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

    Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

    Example 1:
    Input: [1, 2, 2, 3, 1]
    Output: 2
    Explanation: 
    The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.
    Example 2:
    Input: [1,2,2,3,1,4,2]
    Output: 6
    """

    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        firstDict, lastDict = {}, {}

        for index, element in enumerate(nums):
            firstDict.setdefault(element, index)
            lastDict[element] = index

        counter = collections.Counter(nums)
        degree = max(counter.values())

        return min(lastDict[element] - firstDict[element] + 1
                   for element in counter if counter[element] == degree)


if __name__ == '__main__':
    solution = Solution()
    assert solution.findShortestSubArray([1, 2, 2, 3, 1]) == 2
    assert solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6
