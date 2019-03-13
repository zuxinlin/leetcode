#! /usr/bin/env python
# coding: utf-8

'''
题目： 独特的电子邮件地址
主题： string

解题思路：
1. 字符串split和replace处理
'''

from itertools import permutations


class Solution(object):
    '''
    '''

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        s = set()

        for email in emails:
            first, second = email.split('@')
            first = first.split('+')[0].replace('.', '')
            s.add(first + '@' + second)

        return len(s)


if __name__ == '__main__':
    solution = Solution()
    assert solution.numUniqueEmails(
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]) == 2
