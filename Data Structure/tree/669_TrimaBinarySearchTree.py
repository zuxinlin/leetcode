#! /usr/env python
# coding: utf-8
'''
Trim a Binary Search Tree
'''


class TreeNode(object):
    """
    树节点类
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
    """

    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        if not root:
            return None

        if root.val < L:
            return self.trimBST(root.right, L, R)

        if root.val > R:
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root


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
    root = solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    # 前序遍历
    solution.first(root)
    print

    # 层次遍历
    solution.level(root)


if __name__ == '__main__':
    main()
