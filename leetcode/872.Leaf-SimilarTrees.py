#! /usr/bin/env python
# coding: utf-8

'''
题目： 叶子相似树 https://leetcode-cn.com/problems/leaf-similar-trees/
主题： tree & depth-frist search

解题思路：
1. 中序遍历二叉树，获取叶子节点
'''


class Solution(object):
    '''
    '''

    def dfs(self, root, result):
        if root is None:
            return

        self.dfs(root.left, result)

        # 叶子节点
        if root.left is None and root.right is None:
            result.append(root.val)

        self.dfs(root.right, result)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        first, second = [], []

        self.dfs(root1, first)
        self.dfs(root2, second)

        return first == second


if __name__ == '__main__':
    solution = Solution()
