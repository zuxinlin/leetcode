#! /usr/bin/env python
# coding: utf-8

'''
题目： 开方
主题： math & binary search

解题思路：
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        l, r = 0, x

        while l <= r:
            mid = l + (r-l)//2

            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1


if __name__ == '__main__':
    solution = Solution()
