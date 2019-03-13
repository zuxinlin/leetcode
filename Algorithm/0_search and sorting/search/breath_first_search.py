#! /usr/bin/env python
# coding: utf-8

import Queue

'''
bfs遍历会由近及远，同一层会先遍历完。bfs总是先访问完同一层的结点，然后才继续访问下一层结点，它最有用的性质是可以遍历一次就生成中心结点到所遍历结点的最短路径，这一点在求无权图的最短路径时非常有用。

1. 创建一个队列，遍历的起始点放入队列
2. 从队列中取出一个元素，打印它，并将其未访问过的子结点放到队列中
3. 重复2，直至队列空

时间复杂度：基本与图的规模成线性关系
空间复杂度：我们看到程序中使用了一个队列，这个队列会在保存一层的结点，当图规模很大时占用内存还是相当可观的了，所以一般会加上一些条件，比如遍历到第N层就停止
'''

def bfs(graph, start):
    visited = set()
    q = Queue.Queue()
    q.put(start)

    while not q.empty():
        # 队列不为空
        u = q.get()
        print u

        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)

def main():
    graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
    bfs(graph, 1)

if __name__ == '__main__':
    main()
