#! /usr/bin/env python
# coding: utf-8

'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Example 2:

Input: 16
Output: true
Example 3:

Input: 218
Output: false

一个数是否是2的幂次方
'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n & (n - 1) == 0 and n > 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.isPowerOfTwo(0) is False
    assert solution.isPowerOfTwo(1) 
    assert solution.isPowerOfTwo(16) 
    assert solution.isPowerOfTwo(218) is False
