#! /usr/bin/env python
# coding: utf-8

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。 
# 
#  
# 
#  参考以下这颗二叉搜索树： 
# 
#       5
#     / \
#    2   6
#   / \
#  1   3 
# 
#  示例 1： 
# 
#  输入: [1,6,3,2,5]
# 输出: false 
# 
#  示例 2： 
# 
#  输入: [1,3,2,6,5]
# 输出: true 
# 
#  
# 
#  提示： 
# 
#  
#  数组长度 <= 1000 
#  
#  👍 245 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """

        def dfs(i, j):
            if i >= j:  # 只有一个节点，正确
                return True

            p = i

            while postorder[p] < postorder[j]:  # 左子树都小于根节点
                p += 1

            m = p  # 右子树开头

            while postorder[p] > postorder[j]:  # 右子树都大于根节点
                p += 1

            return p == j and dfs(i, m - 1) and dfs(m, j - 1)

        return dfs(0, len(postorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)
