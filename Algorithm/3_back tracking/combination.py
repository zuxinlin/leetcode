#! /usr/bin/env python
# coding: utf-8
"""
组合问题
"""


def combination(arr, m):
    """
    组合，从数组中选出m个元素
    """
    length = len(arr)
    solution = [0] * length  # 一个解（n元0,1数组） 固定长度
    solution_all = []  # 一组解

    def conflict(k):
        """
        冲突检测：无
        """

        # 部分解的长度超出r
        if sum(solution[:k + 1]) > m:
            return True

        # 部分解的长度加上剩下长度不够r
        if sum(solution[:k + 1]) + (length - k - 1) < m:
            return True

        return False  # 无冲突

    def comb(k):
        """
        回溯解空间
        """

        # 退出条件
        if k >= length:
            solution_all.append(solution[:])
        else:
            # 枚举solution[k]所有的可能值，两种选择状态:1-选择，0-不选
            for i in [1, 0]:
                solution[k] = i

                # 剪枝
                if not conflict(k):
                    comb(k + 1)

                # 回溯
                solution[k] = 0

    comb(0)

    for i in solution_all:
        for (index, j) in enumerate(i):
            if j == 1:
                print arr[index],

        print


def main():
    """
    main执行函数
    """
    combination([1, 2, 3, 4], 2)


if __name__ == '__main__':
    main()
