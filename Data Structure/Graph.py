#! /usr/bin/env python
# coding: utf-8

import Queue
import sys

'''
图
'''


class Node(object):
    '''
    节点
    '''

    def __init__(self, value=-1):
        self.value = value      # 节点值
        self.come = 0           # 节点入度
        self.out = 0            # 节点出度
        self.nexts = []         # 节点的邻居节点
        self.edges = []         # 在节点为from的情况下，边的集合


class Edge(object):
    '''
    边
    '''

    def __init__(self, weight, fro, to):
        self.weight = weight        # 边的权重
        self.fro = fro              # 边的from节点
        self.to = to                # 边的to节点

# 图结构


class Graph(object):
    def __init__(self):
        self.nodes = {}     # 图的所有节点集合  字典形式：{节点编号：节点}
        self.edges = []     # 图的边集合

    def create(self, matrix):
        '''
        matrix元素分别代表 from节点，to节点，权重
        '''

        for edge in matrix:
            fro, to, weight = edge

            if fro not in self.nodes:
                self.nodes[fro] = Node(fro)

            if to not in self.nodes:
                self.nodes[to] = Node(to)

            fromNode = self.nodes[fro]
            toNode = self.nodes[to]
            newEdge = Edge(weight, fromNode, toNode)
            fromNode.nexts.append(toNode)
            fromNode.out += 1
            toNode.come += 1
            fromNode.edges.append(newEdge)
            self.edges.append(newEdge)

    def bfs(self, node):
        '''
        基本遍历：图的广度优先遍历
        1.利用队列实现
        2.从源节点开始依次按照宽度进队列，然后弹出
        3.每弹出一个节点，就把该节点所有没有进过队列的邻接点放入队列
        4.直到队列变空
        '''

        if node is None:
            return

        queue = Queue.Queue()
        visit_set = set()
        queue.put(node)
        visit_set.add(node)

        while not queue.empty():
            cur = queue.get()               # 弹出元素
            print cur.value, '->',          # 打印元素值

            for next in cur.nexts:          # 遍历元素的邻接节点
                if next not in visit_set:   # 若邻接节点没有入过队，加入队列并登记
                    visit_set.add(next)
                    queue.put(next)

    def dfs(self, node):
        '''
        基本遍历：图的深度优先遍历
        1.利用栈实现
        2.从源节点开始把节点按照深度放入栈，然后弹出
        3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
        4.直到栈变空
        '''

        if node is None:
            return

        stack = [node]
        visit_set = set([node])
        print node.value, '->',

        while stack:
            cur = stack.pop()                # 弹出最近入栈的节点

            for next in cur.nexts:           # 遍历该节点的邻接节点
                if next not in visit_set:    # 如果邻接节点不重复
                    # stack.append(cur)      # 把节点压入
                    stack.append(next)       # 把邻接节点压入
                    visit_set.add(next)      # 登记节点
                    print next.value, '->',  # 打印节点值
                    break                    # 退出，保持深度优先

    def prim(self, node):
        '''
        最小生成树：普里姆算法
        使用贪心的思想，每一步都选权重最小的边
        '''

        pass

    def kruskal(self, node):
        '''
        最小生成树：克鲁斯卡尔算法
        '''
        pass

    def dijkstra(self, node):
        pass


def main():
    graph = Graph()
    graph.create([[1, 2, 5], [1, 3, 3], [3, 4, 2], [2, 4, 1]])

    print '广度优先遍历：'
    graph.bfs(graph.nodes[1])
    print
    print

    print '深度优先遍历：'
    graph.dfs(graph.nodes[1])


if __name__ == '__main__':
    main()
