#! /usr/bin/env python
# coding: utf-8

import Queue
import sys
import random

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
                    stack.append(next)       # 把邻接节点压入
                    visit_set.add(next)      # 登记节点
                    print next.value, '->',  # 打印节点值
                    break                    # 退出，保持深度优先

    def prim(self, graph):
        '''
        最小生成树：普里姆算法
        使用贪心的思想，每一步都选权重最小的边
        所有节点分成两个group，一个为已经选取的selected_node（为list类型），一个为candidate_node，首先任取一个节点加入到selected_node，然后遍历头节点在selected_node，尾节点在candidate_node的边，选取符合这个条件的边里面权重最小的边，加入到最小生成树，选出的边的尾节点加入到selected_node，并从candidate_node删除。直到candidate_node中没有备选节点（这个循环条件要求所有节点都有边连接，即边数要大于等于节点数-1，循环开始前要加入这个条件判断，否则可能会有节点一直在candidate中，导致死循环）
        '''
        vertex_num = len(graph)
        INF = float('inf')
        visit = [False] * vertex_num
        dist = [INF] * vertex_num  # 访问节点到未访问节点j的最短距离
        visit[0] = True

        # 初始化到顶点0的距离
        for i in range(vertex_num):
            dist[i] = graph[0][i]

        for _ in range(vertex_num-1):
            min_dist = INF
            nextIndex = -1

            for j in range(1, vertex_num):
                if dist[j] < min_dist and not visit[j]:
                    # 得到到访问顶点到未访问顶点的最短路径以及对应顶点
                    min_dist = dist[j]
                    nextIndex = j

            print nextIndex,
            visit[nextIndex] = True

            for j in range(1, vertex_num):
                if dist[j] > graph[nextIndex][j] and not visit[j]:
                    # 此时，访问过的集合里面多了一个顶点，要重新更新最短路径以及对应的顶点
                    dist[j] = graph[nextIndex][j]

        return dist

    def kruskal(self):
        '''
        最小生成树：克鲁斯卡尔算法
        先对边按权重从小到大排序，先选取权重最小的一条边，如果该边的两个节点均为不同的分量，则加入到最小生成树，否则计算下一条边，直到遍历完所有的边
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


def create_graph(N=5):
    graph = [[0]*N for _ in range(N)]
    INF = float('inf')
    distance = range(1, 6) + [INF]

    for i in range(N):
        for j in range(i, N):
            if i != j:
                graph[i][j] = distance[random.randint(0, 5)]
                graph[j][i] = graph[i][j]

    return graph


def print_graph(graph):
    N = len(graph)
    for i in range(N):
        for j in range(N):
            print '%-3s' % graph[i][j],
        print


if __name__ == '__main__':
    # main()
    data = create_graph()
    print_graph(data)
    graph = Graph()
    print graph.prim(data)
