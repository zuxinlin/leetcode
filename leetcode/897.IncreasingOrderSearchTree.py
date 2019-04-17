#! /usr/bin/env python
# coding: utf-8

'''
题目： 递增顺序查找树 https://leetcode-cn.com/problems/increasing-order-search-tree/
主题： tree & depth-first search

解题思路：
1. 中序遍历二叉树
'''


class Solution(object):
    '''
    '''

    def dfs(self, root, tail=None):
        if not root:
            return tail

        res = self.dfs(root.left, root)
        root.left = None
        root.right = self.dfs(root.right, tail)

        return res

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # 中序遍历
        if root is None:
            return None

        stack = []
        result = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current)
            current = current.right

        # 从第一个节点开始右连接
        root = result[0]
        current = root
        current.left = None

        for node in result[1:]:
            current.right = node
            current.left = None
            current = node

        result[-1].left = None
        result[-1].right = None

        return root


if __name__ == '__main__':
    solution = Solution()
    print solution.increasingBST(None)
