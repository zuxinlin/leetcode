#! /usr/bin/env python
# coding: utf-8

from itertools import combinations

'''
题目： 子集
主题： array & backtracking & bit manipulation

解题思路：
1. 迭代
2. 递归，考虑在n - 1个数里面选 k - 1个，然后加上最后一个
3. 回溯
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = [[]]

        # for num in sorted(nums):
        #     res += [item + [num] for item in res]

        # return res

        result = []
        nums.sort()

        def dfs(solution=[], start=0):
            result.append(list(solution))

            for i in xrange(start, len(nums)):
                solution.append(nums[i])
                dfs(solution, i + 1)
                solution.pop()

        dfs()

        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.subsets([5, 4])
