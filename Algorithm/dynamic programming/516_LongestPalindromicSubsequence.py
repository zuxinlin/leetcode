#! /usr/bin/env python
# coding: utf-8
"""
Longest Palindromic Subsequence
"""


class Solution(object):
    """
    Given a string s, find the longest palindromic subsequence's length in s.
    You may assume that the maximum length of s is 1000.

    Example 1:
    Input: "bbbab"
    Output: 4
    One possible longest palindromic subsequence is "bbbb".

    Example 2:
    Input: "cbbd"
    Output: 2
    One possible longest palindromic subsequence is "bb".
    """

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == s[::-1]:
            return len(s)

        l = len(s)
        '''
        the longest palindromic subsequence's length of substring(i, j)
        1. dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
        2. dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
        3. Initialization:dp[i][i] = 1
        '''
        dp = [[0] * l for _ in xrange(l)]

        for i in xrange(l - 1, -1, -1):
            dp[i][i] = 1

            for j in xrange(i + 1, l):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][l - 1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestPalindromeSubseq('bbbab') == 4
    assert solution.longestPalindromeSubseq('aaa') == 3
    assert solution.longestPalindromeSubseq('cbbd') == 2
