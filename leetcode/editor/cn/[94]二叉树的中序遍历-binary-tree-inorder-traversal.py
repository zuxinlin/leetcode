#! /usr/bin/env python
# coding: utf-8

# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1,2]
# 输出：[2,1]
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [1,null,2]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 925 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归
        # result = []
        #
        # def dfs(node):
        #     if not node:
        #         return
        #
        #     dfs(node.left)
        #     result.append(node.val)
        #     dfs(node.right)
        #
        # dfs(root)
        #
        # return result

        # 非递归
        stack, cur, result = [], root, []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        return result
# leetcode submit region end(Prohibit modification and deletion)
