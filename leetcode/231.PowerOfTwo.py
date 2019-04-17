#! /usr/bin/env python
# coding: utf-8

'''
题目： 是否2的n次方
主题： bit manipulation

解题思路：
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
