#! /usr/bin/env python
# coding: utf-8

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

给定数字字符串，可以翻译成多少种ASCII字符串
状态转移方程：dp[i] = (dp[i+1] if a[i] > 0)+ (dp[i+2] if 0 < a[i-1:i+1] <= 26 else 0)，
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) + 1):
            if s[i - 1] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i - 1]
                
                if '1' == s[i-2] or ('2' == s[i-2] and s[i-1] < '7'):
                    dp[i] = dp[i] + dp[i - 2]
                    

        return dp[len(s)]


if __name__ == '__main__':
    solution = Solution()
    assert solution.numDecodings('12') == 2
    assert solution.numDecodings('226') == 3
