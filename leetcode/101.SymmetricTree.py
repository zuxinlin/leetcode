#! /usr/bin/env python
# coding: utf-8

'''
题目： 对称树 https://leetcode-cn.com/problems/symmetric-tree/
主题： tree & depth-first search & breadth-first search

解题思路：
1. 深度优先遍历，比较左右子树
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(left, right):
            if left and right and left.val == right.val:
                return isSym(left.left, right.right) and isSym(left.right, right.left)

            return left == right

        return isSym(root, root)


if __name__ == '__main__':
    pass
