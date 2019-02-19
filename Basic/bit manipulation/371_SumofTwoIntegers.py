#! /usr/bin/env python
# coding: utf-8

'''
Calculate the sum of two integers a and b, but you are not allowed
to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''


class Solution(object):
    

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        # 对于二进制数的而言，对应位相加就可以使用异或（xor）操作，
        # 计算进位就可以使用与（and）操作，在下一步进行对应位相加前，对进位数使用移位操作（<<）。
        # 32 bits integer max
        MAX = 0x7FFFFFFF

        # 32 bits interger min
        MIN = 0x80000000

        # mask to get last 32 bits
        mask = 0xFFFFFFFF

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= MAX else ~(a ^ mask)


if __name__ == '__main__':
    solution = Solution()
    assert solution.getSum(-2, -1) == -3
