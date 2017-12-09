#! /usr/bin/env python
# coding: utf-8

"""
Counting Bits
"""

class Solution(object):
    """
    Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
    calculate the number of 1's in their binary representation and return them as an array.

    Example:
    For num = 5 you should return [0,1,1,2,1,2].

    Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can
    you do it in linear time O(n) /possibly in a single pass? Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount
    in c++ or in any other language.
    """

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        # 1. 找规律：从1开始，遇到偶数时，其1的个数和该偶数除以2得到的数字的1的个数相同，
        # 遇到奇数时，其1的个数等于该奇数除以2得到的数字的1的个数再加1
        # l = []
        #
        # for i in xrange(num + 1):
        #     if i == 0:
        #         l.append(0)
        #     elif i == 1:
        #         l.append(1)
        #     else:
        #         if i % 2 == 0:
        #             l.append(l[i/2])
        #         else:
        #             l.append(l[i/2] + 1)
        #
        # return l

        # 2. 利用移位运算,f(x) = f(x/2) + (x & 1)
        # l = [0]
        #
        # for x in range(1, num + 1):
        #     l.append(l[x >> 1] + (x & 1))
        #
        # return l

        # 3. 按位与运算，f(n & n - 1)如果为0，可以判断f(n)为2的指数
        l = [0]

        for x in range(1, num + 1):
            l.append(l[x & (x - 1)] + 1)

        return l


if __name__ == '__main__':
    solution = Solution()
    assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
