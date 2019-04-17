#! /usr/bin/env python
# coding: utf-8

'''
题目： 数字中1的个数
主题： bit manipulation

解题思路：
1. 左移，解决负数问题
2. 右移
3. n & (n - 1)
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
