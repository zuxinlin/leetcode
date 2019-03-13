#! /usr/bin/env python
# coding: utf-8

'''
题目： 唯一摩尔斯密码词 https://leetcode-cn.com/problems/unique-morse-code-words/
主题： string

解题思路：
1. 
'''


class Solution(object):
    '''
    '''

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                "--.-", ".-.", "...", "-", "..-", "...-", ".--",
                "-..-", "-.--", "--.."]
        s = set()

        for word in words:
            temp = ''

            for c in word:
                temp += code[ord(c) - 97]

            s.add(temp)

        return len(s)


if __name__ == '__main__':
    solution = Solution()
    assert 2 == solution.uniqueMorseRepresentations(
        ["gin", "zen", "gig", "msg"])
