#! /usr/bin/env python
# coding: utf-8

'''
题目： 产生括号
主题： string & backtracking

解题思路：
方法1：递归，dfs
方法2：回溯
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def dfs(s='', left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
            else:
                if left < n:
                    dfs(s + '(', left + 1, right)

                if right < left:
                    dfs(s + ')', left, right + 1)

        dfs()

        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.generateParenthesis(3)
