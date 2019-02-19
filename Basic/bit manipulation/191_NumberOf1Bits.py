#! /usr/bin/env python
# coding: utf-8

'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000

一个数二进制中1的个数
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 调用库函数
        # return bin(n).count('1')

        # 与运算
        counter = 0

        while n:
            n &= n - 1
            counter += 1

        return counter


if __name__ == '__main__':
    solution = Solution()
    assert solution.hammingWeight(11) == 3
    assert solution.hammingWeight(128) == 1
