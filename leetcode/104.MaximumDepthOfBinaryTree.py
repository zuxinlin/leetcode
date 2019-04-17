#! /usr/bin/env python
# coding: utf-8

'''
题目： 二叉树的最大深度 https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
主题： tree & depth-first search

解题思路：
1. 深度优先遍历，看左子树高还是右子树高，然后加1
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    pass
