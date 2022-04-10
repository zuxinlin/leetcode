#!/bin/env python
# coding: utf-8

# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 1136 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_num, col_num = len(grid), len(grid[0])

        if row_num == 0 or col_num == 0:
            return 0

        result = 0

        # bfs
        # for i in range(row_num):
        #     for j in range(col_num):
        #         if grid[i][j] == '1':
        #             result += 1
        #             grid[i][j] = '2' # 将格子标记为「已遍历过」
        #             queue = collections.deque([(i, j)])
        #
        #             while queue:
        #                 row, col = queue.popleft()
        #
        #                 # 访问上、下、左、右四个相邻结点
        #                 for x, y in (
        #                         (row - 1, col), (row + 1, col), (row, col - 1),
        #                         (row, col + 1)):
        #                     if 0 <= x < row_num and 0 <= y < col_num and \
        #                             grid[x][y] == '1':
        #                         grid[x][y] = '2'
        #                         queue.append((x, y))

        # dfs
        def dfs(grid, row, col):
            grid[row][col] = '0'

            # 访问上、下、左、右四个相邻结点
            for x, y in ((row - 1, col), (row + 1, col), (row, col - 1), (row,
                                                                          col + 1)):
                if 0 <= x < row_num and 0 <= y < col_num and grid[x][y] == '1':
                    dfs(grid, x, y)

        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == '1':
                    result += 1
                    dfs(grid, i, j)

        return result


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
