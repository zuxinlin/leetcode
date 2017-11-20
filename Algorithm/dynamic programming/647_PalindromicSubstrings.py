# coding: utf-8

'''
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different
substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
'''


class Solution(object):
    def manachers(self, s):
        a = '@#' + '#'.join(s) + '#$'
        z = [0] * (len(a))
        right = 0
        center = 0

        for i in range(1, len(z) - 1):
            if i < right:
                z[i] = min(right - i, z[2 * center - i])

            while a[i + z[i] + 1] == a[i - z[i] - 1]:
                z[i] += 1

            if i + z[i] > right:
                center = i
                right = i + z[i]

        return z

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 这是一道dp的题，从左到右遍历字符串，每次加进一个字符，递推公式为dp[i]=dp[i-1]+tmpNum。
        # 其中，tmpNum为新加进一个字符后新增加的回文子串的个数。当遍历到index=i时，
        # 只要看看在i之前的index j，能否构成substring(j,i+1)的回文子串。
        # 最后结果是dp[len-1]+len，其中len为字符串的长度，因为字符串每个字符都为回文子串。
        # l = len(s)
        # dp = [1,] * l
        #
        # for i in xrange(1, l):
        #     tmp_num = 1
        #
        #     for j in xrange(i):
        #         ss = s[j: i + 1]
        #
        #         if ss == ss[::-1]:
        #             tmp_num += 1
        #
        #     dp[i] = dp[i - 1] + tmp_num
        #
        # return dp[l - 1]

        # 暴力搜索，默认每个字符都是一个回文串，主要考虑加入一个字符后回文串是多少
        l = len(s)
        count = l

        for i in xrange(1, l):
            for j in xrange(i):
                ss = s[j: i + 1]

                if ss == ss[::-1]:
                    count += 1

        return count


if __name__ == '__main__':
    solution = Solution()
    print solution.manachers('abc')
    assert solution.countSubstrings('abc') == 3
    assert solution.countSubstrings('aaa') == 6
