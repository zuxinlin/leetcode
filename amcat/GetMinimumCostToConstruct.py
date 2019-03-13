#! /usr/bin/env python
# coding: utf-8

import sys


def find(C, u):
    '''
    查
    '''

    while C[u] != u:
        u = C[u]  # 一直传递下去，只要 C[u] != u

    return u


def union(C, u, v):
    '''
    并
    '''
    u = find(C, u)
    v = find(C, v)
    C[u] = v


def kruskal(nodes, edges):
    MST = []
    C = {node: node for node in nodes}
    edges = sorted(edges, key=lambda element: element[2])
    # 对所有的边按权重升序排列
    for u, v, weight in edges:
        if find(C, u) != find(C, v):
            MST.append((u, v, weight))
            union(C, u, v)

    return MST


def prim(maps, nodenum, edgenum):
    res = []

    if nodenum <= 0 or edgenum < nodenum-1:
        return res

    res = []
    seleted_node = [0]
    candidate_node = [i for i in range(1, nodenum)]

    while len(candidate_node) > 0:
        begin, end, minweight = 0, 0, 9999
        for i in seleted_node:
            for j in candidate_node:
                if maps[i][j] < minweight:
                    minweight = maps[i][j]
                    begin = i
                    end = j
        res.append([begin, end, minweight])
        seleted_node.append(end)
        candidate_node.remove(end)
    return res


def getMinimumCostToConstruct(numTotalAvailableCities,
                              numTotalAvailableRoads,
                              roadsAvailable,
                              numNewRoadsConstruct,
                              costNewRoadsConstruct):
    # WRITE YOUR CODE HERE
    nodes = set([city for city in range(1, numTotalAvailableCities + 1)])
    edges = []

    for road in roadsAvailable:
        start, end = road
        edges.append([start, end, 0])

    for road in costNewRoadsConstruct:
        start, end, cost = road
        edges.append([start, end, cost])

    print kruskal(nodes, edges)


def main():
    # print getMinimumCostToConstruct(6, 4, [[1, 2], [2, 3], [4, 5], [3, 5]], 2, [
    #                                 [1, 6, 410], [2, 4, 800]])
    print getMinimumCostToConstruct(6, 4, [[1, 2], [2, 3], [4, 5], [5, 6]], 3, [
                                    [1, 5, 110], [2, 4, 84], [3, 4, 79]])


if __name__ == '__main__':
    main()
