#! /usr/bin/env python
# coding: utf-8

'''
题目： 电话号码字母组合
主题： string & backtracking

解题思路：
方法1：递归，dfs
方法2：回溯
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        key_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []

        if len(digits) == 0:
            return result
        # elif len(digits) == 1:
        #     return list(key_map[digits[0]])
        # else:
        #     pre = self.letterCombinations(digits[:-1])

        #     return [i + j for i in pre for j in key_map[digits[-1]]]

        def dfs(index=0, path=''):
            # 得到解空间
            if len(path) == len(digits):
                result.append(path)
            else:
                # 每一步解的取值范围
                for i in key_map[digits[index]]:
                    dfs(index + 1, path + i)

        dfs()

        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.letterCombinations('23')
