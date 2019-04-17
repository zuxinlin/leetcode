# coding: utf-8

'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

import os


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return '1'

        temp = self.countAndSay(n-1)
        ret = ''
        cnt = 0

        for i in range(len(temp)):
            if i > 0 and temp[i] != temp[i - 1]:
                ret += str(cnt) + temp[i - 1]
                cnt = 1
            else:
                cnt += 1

        ret += str(cnt) + temp[-1]

        return ret



if __name__ == '__main__':
    solution = Solution()
    assert solution.countAndSay(4) == '1211'