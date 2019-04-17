#! /usr/bin/env python
# coding: utf-8


import collections

'''
题目：
主题：

解题思路：

'''

class Solution(object):
    '''
    '''

    def findShortestSubArray(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''

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
