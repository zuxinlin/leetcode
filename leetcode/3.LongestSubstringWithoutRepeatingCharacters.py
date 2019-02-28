#! /usr/bin/env python
# coding: utf-8

'''
题目： 无重复字符的最长子串 https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
主题： hash table & two pointers & string

解题思路：
1. 双头指针，从左往右扫描，中间扫描过的结果可以复用，控制好指针偏移方式
'''


class Solution(object):
    '''
    '''

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        if len(s) < 2:
            return 1

        max_len, left, right = 0, 0, 1
        sub_str = s[left]

        while right < len(s):
            if s[right] in sub_str:
                max_len = max(1, max_len)

                if left == right - 1:
                    right += 1

                left += 1
            else:
                max_len = max(right - left + 1, max_len)
                right += 1

            sub_str = s[left:right]

        return max_len


if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLongestSubstring('abcabcbb') == 3
    assert solution.lengthOfLongestSubstring('bbbbb') == 1
