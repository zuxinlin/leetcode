#! /usr/bin/env python
# coding: utf-8
"""
八皇后问题
"""


def get_n_queen(length):
    """
    8×8格的国际象棋上摆放八个皇后，使其不能互相攻击，即任意两个皇后都不能处于同一行、同一列或同一斜线上，问有多少种摆法。

    为了简化问题，考虑到8个皇后不同行，则每一行放置一个皇后，每一行的皇后可以放置于第0、1、2、...、7列，我们认为每一行的皇后有8种状态。那么，我们只要套用子集树模板，从第0行开始，自上而下，对每一行的皇后，遍历它的8个状态即可。
    """

    solution = [0] * length  # 一个解（n元0,1数组） 固定长度
    solution_all = []  # 一组解

    def conflict(k):
        """
        冲突检测：无
        """

        # 如果发现在同一列或者同一斜线上
        for i in range(k):
            if solution[i] == solution[k] or (
                    k - i) == abs(solution[k] - solution[i]):
                return True

        return False

    def queen(k):
        """
        回溯解空间
        """

        # 退出条件
        if k >= length:
            solution_all.append(solution[:])
        else:
            # 枚举solution[k]所有的可能值，n皇后的话有n个位置可以选择
            for i in range(length):
                solution[k] = i

                # 剪枝
                if not conflict(k):
                    queen(k + 1)

                # 回溯
                solution[k] = 0

    def show(solution):
        """
        解的可视化（根据一个解x，复原棋盘。'X'表示皇后）
        """

        for i in range(length):
            print '. ' * (solution[i]) + 'X ' + '. ' * (
                length - solution[i] - 1)

    queen(0)

    if len(solution_all) == 0:
        print '没有解决方案'

    for solution in solution_all:
        show(solution)
        print


def main():
    """
    main执行函数
    """

    get_n_queen(4)


if __name__ == '__main__':
    main()
