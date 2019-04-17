#! /usr/bin/env python
# coding: utf-8

'''
题目：
主题：

解题思路：
状态转移方程：dp[i][j] = dp[i-1][j-1] if s1[i] == s2[j] else min(dp[i][j-1] + s2[j], dp[i-1][j] + s2[i])
'''


class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        # dp[i][j] is the cost for s1.substr(0,i) and s2.substr(0, j).
        # Note s1[i], s2[j] not included in the substring.
        # Base case: dp[0][0] = 0
        # target: dp[m][n]
        #
        # if s1[i-1] = s2[j-1]   // no deletion
        # dp[i][j] = dp[i-1][j-1];
        # else   // delete either s1[i-1] or s2[j-1]
        # dp[i][j] = min(dp[i-1][j]+s1[i-1], dp[i][j-1]+s2[j-1]);
        l1 = len(s1) + 1
        l2 = len(s2) + 1
        dp = [[0] * l2 for _ in xrange(l1)]

        for j in xrange(1, l2):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in xrange(1, l1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

            for j in xrange(1, l2):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]),
                                   dp[i][j - 1] + ord(s2[j - 1]))

        return dp[l1 - 1][l2 - 1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.minimumDeleteSum('sea', 'eat') == 231
    assert solution.minimumDeleteSum('delete', 'leet') == 403
