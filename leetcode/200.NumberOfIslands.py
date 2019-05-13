#! /usr/bin/env python
# coding: utf-8

'''
题目：岛屿数量 
主题：union find && dfs & bfs

解题思路：
1. 广度优先遍历，如果不是是岛屿，把1至0，一直到不为1的地方
2. 深度优先遍历，类似
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        row, column = len(grid), len(grid[0])

        def bfs():
            count = 0

            for i in range(row):
                for j in range(column):
                    if grid[i][j] == "1":
                        count += 1
                        stack = [(i, j)]

                        for ii, jj in stack:
                            if 0 <= ii < row and 0 <= jj < column and grid[ii][jj] == "1":
                                grid[ii][jj] = "0"
                                stack.extend(
                                    [(ii+1, jj), (ii-1, jj), (ii, jj+1), (ii, jj-1)])

            return count

        return bfs()
#         def dfs(i, j):
#             if i < 0 or i >= row or j < 0 or j >= column or grid[i][j] == '0':
#                 return

#             grid[i][j] = '0'

#             for direction in directions:
#                 dfs(i+direction[0], j+direction[1])


#         count = 0
#         for i in range(row):
#             for j in range(column):
#                 if grid[i][j] == '1':
#                     dfs(i, j)
#                     count += 1

#         return count


if __name__ == '__main__':
    solution = Solution()
    assert solution.numIslands([['1', '1', '1', '1', '0'],
                                ['1', '1', '0', '1', '0'],
                                ['1', '1', '0', '0', '0'],
                                ['0', '0', '0', '0', '0'], ]) == 1
    assert solution.numIslands([['1', '1', '0', '0', '0'],
                                ['1', '1', '0', '0', '0'],
                                ['0', '0', '1', '0', '0'],
                                ['0', '0', '0', '1', '1'], ]) == 3
