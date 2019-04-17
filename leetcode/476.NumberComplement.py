#! /usr/bin/env python
# coding: utf-8

'''
Given a positive integer, output its complement number. The complement strategy
is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits),
and its complement is 0. So you need to output 0.
'''


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        # 求出一个数的二进制数所有位都取反，a ^ b = c, a是已知，c所有位数为1
        # b = c ^ a, bin函数返回二进制字符串，包含0b开头，所以需要减掉2
        # return num ^ (2 ** (len(bin(num)) - 2) - 1)

        # 左移位找到c，所有的位都是1
        i = 1

        while i <= num:
            i <<= 1

        return (i - 1) ^ num


if __name__ == '__main__':
    solution = Solution()
    assert 2 == solution.findComplement(5)
    assert 0 == solution.findComplement(1)
