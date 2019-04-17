#! /usr/bin/env python
# coding: utf-8

'''
题目： 二叉树中序遍历 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
主题： hash table & stack & tree

解题思路：
1. 深度优先遍历，左 根 右
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorder(self, root, result):
        if root is None:
            return

        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)

    def inorder_stack(self, root):
        if root is None:
            return

        stack = []
        current = root
        result = []

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right

        return result

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        self.inorder(root, result)

        return result
        # return self.inorder_stack(root)


if __name__ == '__main__':
    pass
