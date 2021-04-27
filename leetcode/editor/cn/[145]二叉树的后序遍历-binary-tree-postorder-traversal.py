#! /usr/bin/env python
# coding: utf-8

# 给定一个二叉树，返回它的 后序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 569 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
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
        #     dfs(node.right)
        #     result.append(node.val)
        #
        # dfs(root)
        #
        # return result

        # 非递归
        stack, cur, result, pre = [], root, [], None

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if not cur.right or cur.right == pre:
                result.append(cur.val)
                pre = cur
                cur = None
            else:
                stack.append(cur)
                cur = cur.right

        return result
# leetcode submit region end(Prohibit modification and deletion)
