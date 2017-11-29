#! /usr/bin/env python
# coding: utf-8
"""
Two Sum II
"""


class Solution(object):
    """
    Given an array of integers that is already sorted in ascending order, find two numbers
    such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they add up to
    the target, where index1 must be less than index2. Please note that your returned answers
    (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution and you may not use the
    same element twice.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2    
    """

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 采用字典存储第一个数的下标
        # d = {}
        # l = len(numbers)
        #
        # for i in xrange(l):
        #     d[numbers[i]] = i
        #
        # for i in xrange(l):
        #     if target - numbers[i] in d:
        #         return [i + 1, d[target - numbers[i]] + 1]

        # 采用二分查找，从两点出发
        l = len(numbers)
        i, j = 0, l - 1

        while i < j:
            s = numbers[i] + numbers[j]

            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return [i + 1, j + 1]


if __name__ == '__main__':
    solution = Solution()
    print solution.twoSum([2, 7, 11, 15], 9)
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
