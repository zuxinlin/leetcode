# coding: utf-8

'''
题目： 最大回文子串 https://leetcode-cn.com/problems/longest-palindromic-substring/
主题： string & dynamic programming

解题思路：
1. 分奇数和偶数，分别向两边扩展，o(n*n)
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 马拉车算法
        # a = '@#' + '#'.join(s) + '#$'
        # P = [0] * (len(a))  # 为新字符串T的T[i]处的回文半径, 数组P有一性质，P[i]-1就是该回文子串在原字符串S中的长度
        # right = 0  # 为该回文串能达到的最右端的值
        # center = 0  # 为最大回文串对应的中心点
        # max_len, max_index = 0, 0
        #
        # for i in range(1, len(P) - 1):
        #     if i < right:
        #         P[i] = min(right - i, P[2 * center - i])
        #
        #     while a[i + P[i]] == a[i - P[i]]:
        #         P[i] += 1
        #
        #     if i + P[i] > right:
        #         center = i
        #         right = i + P[i]
        #
        #     if P[i] > max_len:
        #         max_len = P[i]
        #         max_point = i
        #
        # return s[(max_point - max_len) / 2:(max_len + max_point) / 2 - 1]

        l = len(s)

        # 边界考虑
        if l <= 2:
            return s

        if s == s[::-1]:
            return s

        # 分字符串长度是奇数，还是偶数，如果已经扫描过最长的，我们只检查是否有比当前最长子串还长的串
        maxLen, start = 0, 0

        for i in range(l):
            # 奇数
            left, right = i - 1, i + 1

            while left >= 0 and right < l and s[left] == s[right]:
                current = right - left

                if current > maxLen:
                    maxLen = current
                    start = left

                left -= 1
                right += 1

            # 偶数
            left, right = i, i + 1

            while left >= 0 and right < l and s[left] == s[right]:
                current = right - left

                if current > maxLen:
                    maxLen = current
                    start = left

                left -= 1
                right += 1

        return s[start:start + maxLen + 1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestPalindrome('cbbd') == 'bb'
    assert solution.longestPalindrome('aaa') == 'aaa'
    assert solution.longestPalindrome('abc') == 'a'
