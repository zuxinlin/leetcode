
#! /usr/bin/env python
# coding: utf-8

'''
题目： 二叉树的最大深度 https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
主题： tree & depth-first search

解题思路：
1. 深度优先遍历，看左子树高还是右子树高，然后加1
'''

import sys
from Queue import Queue


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.depth = sys.maxint

    def dfs(self, root, depth):
        if root.left is None and root.right is None:
            self.depth = min(self.depth, depth)

        if root.left:
            self.dfs(root.left, depth + 1)

        if root.right:
            self.dfs(root.right, depth + 1)

    def bfs(self, root):
        if root is None:
            return 0

        queue = Queue()
        queue.put(root)
        level = 1
        current = 0
        last = 1

        while not queue.empty():
            current = queue.get()

            if current.left is None and current.right is None:
                return level

            last -= 1

            if current.left:
                queue.put(current.left)
                current += 1

            if current.right:
                queue.put(current.right)
                current += 1

            if last == 0:
                last = current
                current = 0
                level += 1


    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        if root.left is None:
            return self.minDepth(root.right) + 1

        if root.right is None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == '__main__':
    pass
