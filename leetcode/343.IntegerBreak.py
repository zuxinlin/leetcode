#! /usr/bin/env python
# coding: utf-8

"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

求给定数字n，拆分为几个数字之和，构成的乘积最大，典型背包问题，返回最大的乘积
状态转移方程：dp[j] = max(dp[j], dp[j-i] * i)，表示和为j时最大的乘积
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        # dp = [0] * (n+1)
        # dp[0] = 1
        # result = 0

        # for i in range(1, n):
        #     for j in range(i, n+1):
        #         dp[j] = max(dp[j], dp[j-i] * i)

        #         if j == n and result < dp[j]:
        #             result = dp[j]

        # return result

        '''
        正整数从1开始，但是1不能拆分成两个正整数之和，所以不能当输出。
        那么2只能拆成1+1，所以乘积也为1。
        数字3可以拆分成2+1或1+1+1，显然第一种拆分方法乘积大为2。
        数字4拆成2+2，乘积最大，为4。
        数字5拆成3+2，乘积最大，为6。
        数字6拆成3+3，乘积最大，为9。
        数字7拆为3+4，乘积最大，为12。
        数字8拆为3+3+2，乘积最大，为18。
        数字9拆为3+3+3，乘积最大，为27。
        数字10拆为3+3+4，乘积最大，为36。

        看出从5开始，数字都需要先拆出所有的3，一直拆到剩下一个数为2或者4，因为剩4就不用再拆了，拆成两个2和不拆没有意义，而且4不能拆出一个3剩一个1，这样会比拆成2+2的乘积小。
        '''
        res = [0, 0, 1, 2, 4]

        if n < 5:
            return res[n]

        k, m = n // 3, n % 3

        if m == 0:
            return 3**k
        elif m == 1:
            return 3**(k-1)*4
        else:
            return 3**k*2


if __name__ == '__main__':
    solution = Solution()
    assert solution.integerBreak(2) == 1
    assert solution.integerBreak(10) == 36
