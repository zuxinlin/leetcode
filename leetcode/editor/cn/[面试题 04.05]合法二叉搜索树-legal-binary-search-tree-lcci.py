#! /usr/bin/env python
# coding: utf-8

# 实现一个函数，检查一棵二叉树是否为二叉搜索树。示例 1: 输入:     2    / \   1   3 输出: true 示例 2: 输入:     5
#     / \   1   4      / \     3   6 输出: false 解释: 输入为: [5,1,4,null,null,3,6]。    
#   根节点的值为 5 ，但是其右子节点值为 4 。 Related Topics 树 深度优先搜索 
#  👍 46 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True

            val = root.val

            if val <= lower or val >= upper:
                return False

            return dfs(root.left, lower, val) and dfs(root.right, val, upper)

        return dfs(root)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
