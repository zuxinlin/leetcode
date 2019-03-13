#! /usr/bin/env python
# coding: utf-8

import os

'''
题目： 最长公共前缀 https://leetcode-cn.com/problems/longest-common-prefix/
主题： math & string

解题思路：
最长公共前缀，先找出最短的字符串，然后从头遍历这个字符串的字符。只要测试验证一个即可
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 调用系统函数
        # return os.path.commonprefix(strs)

        if len(strs) == 0:
            return ''

        min_len = len(strs[0])
        min_str = strs[0]

        for s in strs[1:]:
            if len(s) < min_len:
                min_len = len(s)
                min_str = s

        for (index, element) in enumerate(min_str):
            for s in strs:
                if s[index] != element:
                    return min_str[:index] if index > 0 else ''

        return min_str


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ''
