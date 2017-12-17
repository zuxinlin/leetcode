#! /usr/bin/env python
# coding: utf-8
"""
迷宫问题
"""


def get_maze_path():
    """
    给定一个迷宫，入口已知。问是否有路径从入口到出口，若有则输出一条这样的路径。注意移动可以从上、下、左、右、上左、上右、下左、下右八个方向进行。迷宫输入0表示可走，输入1表示墙。为方便起见，用1将迷宫围起来避免边界问题

    考虑到左、右是相对的，因此修改为：北、东北、东、东南、南、西南、西、西北八个方向。在任意一格内，有8个方向可以选择，亦即8种状态可选。因此从入口格子开始，每进入一格都要遍历这8种状态。
    """

    # 迷宫（1是墙，0是通路）
    maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 0, 1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]

    line, column = 8, 10  # 8行，10列
    entry = (1, 0)  # 迷宫入口
    path = [entry]  # 一个解（路径），长度不固定
    paths = []  # 一组解
    # 移动的方向（顺时针8个：N, EN, E, ES, S, WS, W, WN）
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1),
                  (-1, -1)]

    def conflict(new_x, new_y):
        """
        冲突检测：无
        """

        # 是否在迷宫里面以及是否可以通行
        if 0 <= new_x < line and 0 <= new_y < column and maze[new_x][new_y] == 0:
            return False

        return True

    def walk(x, y):
        """
        到达(x,y)格子
        """

        if (x, y) != entry and (x % (line - 1) == 0 or y % (column - 1) == 0):
            paths.append(path[:])
        else:
            # 枚举mazy[x][y]所有可能值，有八个方向可以选择
            for i in directions:
                maze[x][y] = 2
                new_x, new_y = x + i[0], y + i[1]
                path.append((new_x, new_y))

                # 剪枝
                if not conflict(new_x, new_y):
                    walk(new_x, new_y)

                # 回溯
                maze[x][y] = 0
                path.pop()

    def show(path):
        """
        解的可视化（根据一个解x，复原棋盘。'X'表示皇后）
        """

        solution = maze[:]

        for i in path:
            solution[i[0]][i[1]] = 2

        for j in solution:
            print j

    walk(entry[0], entry[1])

    for path in paths:
        show(path)
        print


def main():
    """
    main执行函数
    """
    get_maze_path()


if __name__ == '__main__':
    main()
