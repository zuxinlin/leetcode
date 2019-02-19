#! /usr/bin/env python
# coding: utf-8

'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

'''

import sys


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

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        else:
            self.dfs(root, 1)

            return self.depth


if __name__ == '__main__':
    pass
