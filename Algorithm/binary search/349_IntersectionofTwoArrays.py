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
    def dfs(self, root, depth, res):
        if res[1] < depth:
            res[0] = root.val
            res[1] = depth

        if root.left:
            self.dfs(root.left, depth + 1, res)

        if root.right:
            self.dfs(root.right, depth + 1, res)

        return res[0]

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.dfs(root, 1, [0, 0])


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    solution = Solution()
    print solution.findBottomLeftValue(root)
