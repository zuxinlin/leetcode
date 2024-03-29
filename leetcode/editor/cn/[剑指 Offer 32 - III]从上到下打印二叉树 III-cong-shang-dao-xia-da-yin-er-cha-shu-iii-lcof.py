#! /usr/bin/env python
# coding: utf-8

# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。 
# 
#  
# 
#  例如: 
# 给定二叉树: [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 1000 
#  
#  Related Topics 树 广度优先搜索 
#  👍 91 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            temp = []
            length = len(queue)

            # 一层层遍历
            for _ in range(length):
                node = queue.pop(0)
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(temp)

        data = []
        for index, item in enumerate(result):
            if index % 2 == 0:
                data.append(item)
            else:
                data.append(item[::-1])
        return data
        # leetcode submit region end(Prohibit modification and deletion)
