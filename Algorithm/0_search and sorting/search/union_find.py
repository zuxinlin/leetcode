#! /usr/bin/env python
# coding: utf-8


class UF(object):
    """并查集类"""

    def __init__(self, n):
        """
        长度为n的并查集
        """
        self.parent = [i for i in range(n + 1)]  # 列表0位置空出
        self.count = n  # 判断并查集里共有几个集合, 初始化默认互相独立
        self.rank = [1 for _ in range(n)]  # 权重避免树高度不均衡

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]  # 路径压缩
            p = self.parent[p]

        return p

    def union(self, p, q):
        """
        连通p,q 让q指向p
        """
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        # 把权重小的挂到权重大的，避免深度太深
        if self.rank[p_root] < self.rank[q_root]:
            # q 所在集合比 p 所在集合节点数多
            # 将 p 所在集合合并到 q 所在集合，并更新 q 所在集合的节点数信息
            self.parent[p_root] = q_root
            self.rank[q_root] += self.rank[p_root]
        elif self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
            self.rank[p_root] += self.rank[q_root]

    self.count -= 1

    def is_connected(self, p, q):
        """判断p和q是否已经连通"""
        return self.find(p) == self.find(q)     # 即判断两个结点是否是属于同一个祖先

    def get_count(self):
        return self.count


def find(data_dict, u):
    """
    查
    """

    while data_dict[u] != u:
        u = data_dict[u]  # 一直传递下去，只要 data_dict[u] != u

    return u


def union(data_dict, u, v):
    """
    并
    """

    u = find(data_dict, u)
    v = find(data_dict, v)
    data_dict[u] = v


def main():
    uf = UF(10)
    data = [[0, 1], [0, 4], [1, 2], [1, 3], [5, 6], [6, 7], [7, 5], [8, 9]]

    for edge in data:
        # p, v = random.randint(0, 9), random.randint(0, 9)
        p, v = edge[0], edge[1]
        print('[%s, %s],' % (p, v))
        uf.union(p, v)

    for node in range(10):
        print('node: %s, root: %s' % (node, uf.find(node)))


if __name__ == '__main__':
    main()
