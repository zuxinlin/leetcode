#! /usr/bin/env python
# coding: utf-8

"""
"""

from itertools import permutations


class Solution(object):
    '''
    Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

    Example 1:

    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Example 2:

    Input: [-7,-3,2,3,11]
    Output: [4,9,9,49,121]
    

    Note:

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.
    '''

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        result = [item**2 for item in A]
        result.sort() # return sorted(result, lambda a, b: a - b)

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert solution.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
