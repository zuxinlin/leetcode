#! /usr/bin/env python
# coding: utf-8

'''
题目： 杨辉三角 https://leetcode-cn.com/problems/pascals-triangle/submissions/
主题： array

解题思路：
1. 
'''

import sys
from Queue import Queue


# Definition for a binary tree node.
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]

        for i in range(2, numRows):
            temp = []

            for index, data in enumerate(result[i - 1]):
                if index == 0:
                    temp.append(1)
                else:
                    temp.append(data + result[i - 1][index - 1])
            temp.append(1)
            result.append(temp)

        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.generate(5)
