#! /usr/bin/env python
# coding: utf-8

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 1025 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # stack = []
        # share = float('-inf')
        #
        # # 中序遍历非递归
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #
        #     root = stack.pop()
        #
        #     if root.val <= share:
        #         return False
        #
        #     share = root.val
        #     root = root.right
        #
        # return True

        # 递归，搜索二叉树特性：左子树所有值小于根节点，右子树所有值大于根节点
        def dfs(root, low=float('-inf'), high=float('inf')):
            if not root:
                return True

            val = root.val

            return low < val < high and dfs(root.left, low, val) and dfs(
                root.right, val, high)

        return dfs(root)

# leetcode submit region end(Prohibit modification and deletion)
