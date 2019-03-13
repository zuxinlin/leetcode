#! /usr/bin/env python
# coding: utf-8

import Queue

'''
顺着起点往下走，直到无路可走就退回去找下一条路径，直到走完所有的结点

栈顶元素表示即将要访问的结点的父结点及其是父结点的第N个子结点

时间复杂度：基本与图的规模成线性关系
空间复杂度：我们看到程序中使用了一个队列，这个队列会在保存一层的结点，当图规模很大时占用内存还是相当可观的了，所以一般会加上一些条件，比如遍历到第N层就停止
'''


def dfs(graph, start):
    visited = set()
    stack = [start]
    print start

    while stack:
        cur = stack.pop() # 弹出最近入栈的节点

        if cur in graph:
            for next in graph[cur]: # 遍历该节点的邻接节点
                if next not in visited: # 如果邻接节点不重复
                    stack.append(cur) # 把节点压入
                    stack.append(next) # 把邻接节点压入
                    print next # 打印节点值
                    visited.add(next) # 登记节点
                    break # 退出，保持深度优先


def main():
    graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
    dfs(graph, 1)


if __name__ == '__main__':
    main()
