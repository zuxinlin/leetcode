#! /usr/bin/env python
# coding: utf-8

# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。 
# 
#  
# 
#  示例: 
# 给定如下二叉树，以及目标和 target = 22， 
# 
#  
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 10000 
#  
# 
#  注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/ 
#  Related Topics 树 深度优先搜索 
#  👍 166 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        path = []

        def dfs(root, target):
            if not root:
                return

            # 前序遍历
            target -= root.val
            path.append(root.val)

            # 从根节点到叶子节点
            if target == 0 and not root.left and not root.right:
                result.append(list(path))
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()

        dfs(root, target)

        return result
# leetcode submit region end(Prohibit modification and deletion)
