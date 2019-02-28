#! /usr/bin/env python
# coding: utf-8

"""
Permutations
"""

from itertools import permutations


class Solution(object):
    '''
    Given a collection of distinct numbers, return all possible permutations.

    For example,
    [1,2,3] have the following permutations:
    [
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
    ]
    '''

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 递归，遍历每个元素
        if len(nums) == 0:
            return [[]]

        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i + 1:])]

        # 使用库函数
        # return list(permutations(nums))


if __name__ == '__main__':
    solution = Solution()
    print solution.permute([1, 2, 3])
    assert solution.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                                           [2, 3, 1], [3, 1, 2], [3, 2, 1]]
