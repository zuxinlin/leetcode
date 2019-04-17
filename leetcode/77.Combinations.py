#! /usr/bin/env python
# coding: utf-8

from itertools import combinations

'''
题目： 组合
主题： array & backtracking & bit manipulation

解题思路：
1. 直接调用库函数
2. 递归，考虑在n - 1个数里面选 k - 1个，然后加上最后一个
3. 回溯
'''


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # 调用库函数，获取组合，c(m, n) = n! / ((n-m)! * m!)
        # return list(combinations(range(1, n + 1), k))

        # if k == 0:
        #     return [[]]

        # return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]

        result = []

        def dfs(temp=[], start=1, count=0):
            # 得到解空间
            if count == k:
                result.append(list(temp))
            else:
                for i in range(start, n + 1):
                    temp.append(i)
                    dfs(temp, i + 1, count+1)
                    temp.pop()

        dfs()

        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.combine(4, 2)
