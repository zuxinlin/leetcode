#! /usr/bin/env python
# coding: utf-8
"""
全排列
"""


def permutation(s, start, end):
    """
    全排列递归
    """
    if start == end:
        print ' '.join(s)

    for i in xrange(start, end + 1):
        s[start], s[i] = s[i], s[start]
        permutation(s, start + 1, end)
        s[start], s[i] = s[i], s[start]


def permutation_new(string):
    """
    全排列非递归
    """
    length = len(string)
    solution = [0] * length  # 一个解（n元0-1数组）
    solution_all = []  # 一组解

    def conflict(k):
        """
        冲突检测：无
        """

        # for i in range(k):
        #     if solution[i] == solution[k]:
        #         return True

        return False  # 无冲突

    def perm(k):
        """
        用子集树模板实现全排列, 到达第k个元素 
        """

        if k >= length:  # 超出最尾的元素
            print ' '.join(solution)
            solution_all.append(solution[:])  # 保存（一个解）
        else:
            # 遍历剩下的未排的所有元素，看作元素solution[k-1]的状态空间
            for i in set(string) - set(solution[:k]):
                solution[k] = i

                if not conflict(k):  # 剪枝
                    perm(k + 1)

                solution[k] = 0

    perm(0)


def main():
    """
    main执行函数
    """
    s = list('ABC')
    # permutation(s, 0, len(s) - 1)
    permutation_new(s)


if __name__ == '__main__':
    main()
