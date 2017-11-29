#! /usr/bin/env python
# coding: utf-8
"""
Combinations
"""

from itertools import combinations


class Solution(object):
    '''
    Given two integers n and k, return all possible combinations of k numbers
    out of 1 ... n.

    For example,
    If n = 4 and k = 2, a solution is:

    [
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
    ]
    '''

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # 调用库函数，获取组合，c(m, n) = n! / ((n-m)! * m!)
        return list(combinations(range(1, n + 1), k))

        # 递归
        # if k == 0:
        #     return [[]]
        #
        # return [pre + [i] for i in range(1, n + 1) for pre in self.combine(i - 1, k - 1)]

        # c()


if __name__ == '__main__':
    solution = Solution()
    print solution.combine(4, 2)
    assert solution.combine(4, 2) == [
        [2, 4],
        [3, 4],
        [2, 3],
        [1, 2],
        [1, 3],
        [1, 4],
    ]
