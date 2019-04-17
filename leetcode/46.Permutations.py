#! /usr/bin/env python
# coding: utf-8

from itertools import permutations

'''
题目： 排列
主题： backtracking

解题思路：
1. 使用库函数
2. 回溯
3. 递归
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def dfs(solution=[]):
            # 跳出条件是已取了池子里所有的数，完成一次排列
            if len(solution) == len(nums):
                result.append(list(solution))
            else:
                for i in nums:
                    # 剪枝逻辑：取过的数不再取
                    if i not in solution:
                        solution.append(i)
                        dfs(solution)
                        solution.pop()

        dfs()

        return result

        # 使用库函数
        # return list(permutations(nums))


if __name__ == '__main__':
    solution = Solution()
    print solution.permute([1, 2, 3])
    assert solution.permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                                           [2, 3, 1], [3, 1, 2], [3, 2, 1]]
