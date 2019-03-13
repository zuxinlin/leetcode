#! /usr/bin/env python
# coding: utf-8

'''
题目： 重复 N 次的元素
主题： hash table

解题思路：
1. 两个字典存储
'''


class Solution(object):
    '''
    '''

    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        dict = {}

        for i in A:
            if i not in dict:
                dict[i] = True
            else:
                return i


if __name__ == '__main__':
    solution = Solution()
    assert solution.repeatedNTimes([1, 2, 3, 3]) == 3
