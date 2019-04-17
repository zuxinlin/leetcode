#! /usr/bin/env python
# coding: utf-8

'''
题目： 二叉树前序遍历 https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
主题： stack & tree

解题思路：
1. 深度优先遍历，根 左 右
'''


class Solution(object):
    def preorder(self, root, result):
        if root:
            result.append(root.val)
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    def preorder_stack(self, root):
        if root:
            stack = []
            current = root
            result = []

            while current or stack:
                if current:
                    stack.append(current)
                    result.append(current.val)
                    current = current.left
                else:
                    current = stack.pop()
                    current = current.right

            return result

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        self.preorder(root, result)

        return result
        # return self.preorder_stack(root)


if __name__ == '__main__':
    pass
