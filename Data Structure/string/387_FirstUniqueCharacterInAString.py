#! /usr/bin/env python
# coding: utf-8
"""
First Unique Character in a String
"""

import string


class Solution(object):
    """
    Given a string, find the first non-repeating character in it and return it's index. 
    If it doesn't exist, return -1.

    Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.
    Note: You may assume the string contain only lowercase letters.
    """

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 先统计每个字符出现次数，然后从前往后遍历，找出出现次数为1的字符
        # d = {}

        # for i in s:
        #     d[i] = d[i] + 1 if d.has_key(i) else 1

        # for (index, element) in enumerate(s):
        #     if d[element] == 1:
        #         return index

        # return -1

        # 遍历26个字母，找出出现一次，并且下标最小的那个
        return min(
            [s.find(c) for c in string.ascii_lowercase if s.count(c) == 1]
            or [-1])


if __name__ == '__main__':
    solution = Solution()
    assert 0 == solution.firstUniqChar('leetcode')
    assert 2 == solution.firstUniqChar('loveleetcode')