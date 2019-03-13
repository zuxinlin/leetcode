#! /usr/bin/env python
# coding: utf-8

'''
题目： 
主题： graph

解题思路：
1. 
'''

from itertools import permutations


class Solution(object):
    '''
    '''

    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        # result = [0] * len(A)
        # even_index = 0
        # odd_index = 1

        # for item in A:
        #     if item % 2 == 0:
        #         result[even_index] = item
        #         even_index += 2
        #     else:
        #         result[odd_index] = item
        #         odd_index += 2

        # return result

        # 2个指针
        odd, even, n = 1, 0, len(A)

        while odd < n and even < n:
            # 奇数索引放偶数，偶数索引放奇数，对调
            if A[odd] % 2 == 0 and A[even] % 2:
                A[odd], A[even] = A[even], A[odd]

            # 奇数位置放对
            if A[odd] % 2 == 1:
                odd += 2

            # 偶数位置放对
            if A[even] % 2 == 0:
                even += 2

        return A


if __name__ == '__main__':
    solution = Solution()
    print solution.sortArrayByParityII([4, 2, 5, 7])
    assert solution.sortArrayByParityII([4,2,5,7]) == [4, 5, 2, 7]
