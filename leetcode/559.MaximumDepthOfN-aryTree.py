# coding: utf-8

from Queue import Queue

'''
题目： N叉树的最大深度 https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/
主题：tree & depth-first search & breath-first search

解题思路：
1. 广度优先遍历，记录每一层高度
2. 深度优先遍历
'''


class Solution(object):
    def bfs(self, root):
        '''
        广度优先遍历，给每个节点记录一下所在深度
        '''

        if root is None:
            return 0
        elif len(root.children) == 0:
            return 1

        queue = Queue()
        queue.put((root, 1))

        while not queue.empty():
            current, depth = queue.get()

            for child in current.children:
                queue.put((child, depth + 1))

        return depth

    def dfs(self, root):
        '''
        深度优先遍历，记录最大深度
        '''

        if root is None:
            return 0
        elif len(root.children) == 0:
            return 1

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            current, depth = stack.pop()

            for child in current.children:
                stack.append((child, depth + 1))

                if depth + 1 > max_depth:
                    max_depth = depth + 1

        return max_depth

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if root is None:
            return 0
        elif len(root.children) == 0:
            return 1

        return max([self.maxDepth(child) for child in root.children]) + 1


if __name__ == '__main__':
    solution = Solution()
    print solution.maxDepth(None)
