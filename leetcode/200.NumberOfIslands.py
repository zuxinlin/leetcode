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

        def bfs(grid):
            '''
            广度优先遍历
            '''
            if not grid:
                return 0

            row, column, count = len(grid), len(grid[0]), 0

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

        def dfs(grid):
            if not grid:
                return 0

            row, column, count = len(grid), len(grid[0]), 0

            for i in range(row):
                for j in range(column):
                    if grid[i][j] == "1":
                        count += 1
                        stack = [(i, j)]

                        while stack:
                            ii, jj = stack.pop()

                            if 0 <= ii < row and 0 <= jj < column and grid[ii][jj] == "1":
                                grid[ii][jj] = "0"
                                stack.extend(
                                    [(ii+1, jj), (ii-1, jj), (ii, jj+1), (ii, jj-1)])
        return bfs(grid)

        # return dfs(grid)

        # def dfs_recursive(grid, i, j):
        #     if 0 <= i < row and 0 <= j < column and grid[i][j] == "1":
        #         grid[i][j] = "0"

        #     dfs_recursive(grid, i-1, j)
        #     dfs_recursive(grid, i+1, j)
        #     dfs_recursive(grid, i, j-1)
        #     dfs_recursive(grid, i, j+1)

        # if not grid:
        #     return 0

        # row, column, count = len(grid), len(grid[0]), 0

        # for i in range(row):
        #     for j in range(column):
        #         if grid[i][j] == "1":
        #             count += 1
        #             dfs_recursive(grid, i, j)

        # return count


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
