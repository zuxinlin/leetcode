#! /usr/bin/env python
# coding: utf-8

'''
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3
Output:1

Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:7
Note: You may assume the tree (i.e., the given root node) is not NULL.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_depth = 0

    def dfs(self, root):
        if root is None:
            return 0

        return max(self.dfs(root.left), self.dfs(root.right)) + 1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)


if __name__ == '__main__':
    pass
