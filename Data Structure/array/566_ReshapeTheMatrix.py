#! /usr/bin/env python
# coding: utf-8
"""
Reshape The Matrix
"""


class Solution(object):
    """
    In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

    You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

    The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

    If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
    """

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return nums

        sourceRow = len(nums)
        sourceColumn = len(nums[0])

        if sourceRow * sourceColumn != r * c:
            return nums
        else:
            result = []

            for i in xrange(r):
                columList = []

                for j in xrange(c):
                    count = i * c + j
                    m = count / sourceColumn
                    n = count % sourceColumn
                    columList.append(nums[m][n])

                result.append(columList)

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 2], [3, 4]]
    print sum(nums, [])

    r = 1
    c = 4
    # nums = [[1, 2, 3, 4]]
    # r = 2
    # c = 2
    assert [[1, 2, 3, 4]] == solution.matrixReshape(nums, r, c)
