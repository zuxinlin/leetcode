#! /usr/bin/env python
# coding: utf-8
"""
回溯通用方法
"""

import time

def backtracking(n, m, check, handle):
    """
    回溯算法非递归实现
    """

    k, a = 0, [-1 for _ in range(m)]

    while k >= 0:
        a[k] += 1

        while a[k] < n and not check(a, k):
            a[k] += 1

        if a[k] == n or k == m:
            k -= 1
        else:
            if k == m - 1:
                handle(a)
            else:
                k += 1
                a[k] = -1


def backtracking_recursive(n, m, check, handle):
    """
    回溯算法递归实现
    n, m决定我们搜索的解空间大小
    n表示每步可选择的状态
    m表示最终方案的元素个数
    check是冲突检查函数
    handle是找到解决方案后的处理函数
    """
    a = [0 for _ in range(m)]

    def dfs(k=0):
        """
        深度优先搜，a存储解决方案结果，k是当前深度
        """

        for i in range(n):
            a[k] = i

            if check(a, k):
                if k == m - 1:
                    handle(a)
                else:
                    dfs(k + 1)

    dfs(0)


def counter(n, m):
    """
    列出全部解空间
    """

    def display(a):
        print a

    backtracking(n, m, lambda a, k: True, display)


def display(solution):
    """
    打印结果
    """

    arr = ['A', 'B', 'C', 'D']

    print ' '.join([arr[solution[i]] for i in range(len(solution))])


def permutation(n, m):
    """
    全排列
    """

    def check(a, k):
        """
        冲突检查，没有冲突返回True，否则返回False
        """

        for i in range(k):
            if a[i] == a[k]:
                return False

        return True

    backtracking(n, m, check, display)


def combination(n, m):
    """
    组合
    """

    def check(solution, k):
        """
        冲突检查，没有冲突返回True，否则返回False
        """

        for i in range(k):
            if solution[i] >= solution[k]:
                return False

        return True

    backtracking(n, m, check, display)

def queen(n):
    """
    n皇后问题
    """

    def check(solution, k):
        """
        冲突检查，没有冲突返回True，否则返回False
        """

        for i in range(k):
            if solution[i] == solution[k] or abs(solution[i] - solution[k]) == k - i:
                return False

        return True

    def handle(solution):
        size = len(solution)

        for i in solution:
            print  '%sX %s' % ('* ' * i, (size - i - 1) * '* ')

        print

    backtracking(n, n, check, handle)


def main():
    start = time.time()

    counter(3, 2)

    print '排列结果：'
    permutation(4, 4)
    print

    print '组合结果：'
    combination(4, 2)
    print

    print '四皇后：'
    queen(4)
    print

    end = time.time()
    print 'take time: %s' % (end - start)


if __name__ == '__main__':
    main()