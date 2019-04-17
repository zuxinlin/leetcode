# coding: utf-8

'''
题目：
主题：

解题思路：
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join([i[::-1] for i in s.split()])
        # return ' '.join(map(lambda s: s[::-1], s.split()))

if __name__ == '__main__':
    solution = Solution()
    print solution.reverseWords('my   name is linzuxin')