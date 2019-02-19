#! /usr/env python
# coding: utf-8

"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Note: The merging process must start from the root nodes of both trees.

合并两颗二叉树
"""


class TreeNode(object):
    """
    树节点类
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if not t1 or not t2:
            return t1 or t2
        elif t1 != None and t2 != None:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)

            return root
        else:
            return None

    def first(self, root):
        """
        前序遍历
        """

        if not root:
            return

        print root.val, '->',
        self.first(root.left)
        self.first(root.right)

    def level(self, root):
        """
        层次遍历
        """

        queue = [root]

        while queue:
            current = queue.pop(0)
            print current.val, '->',

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)


def main():
    """
    main函数
    """

    solution = Solution()


if __name__ == '__main__':
    main()
