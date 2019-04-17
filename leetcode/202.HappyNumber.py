#! /usr/bin/env python
# coding: utf-8

'''
题目： 高兴数字 
主题： hash table & math

解题思路：
1. 重复直接返回False
'''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        mem = set()

        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])

            if n in mem:
                return False
            else:
                mem.add(n)

        return True


if __name__ == '__main__':
    solution = Solution()
