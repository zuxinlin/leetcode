#! /usr/bin/env python
# coding: utf-8

# 请实现两个函数，分别用来序列化和反序列化二叉树。 
# 
#  示例: 
# 
#  你可以将以下二叉树：
# 
#     1
#    / \
#   2   3
#      / \
#     4   5
# 
# 序列化为 "[1,2,3,null,null,4,5]" 
# 
#  注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-b
# inary-tree/ 
#  Related Topics 树 设计 
#  👍 146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'

        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')

        return '[' + (','.join(result)) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return

        values, i = data[1:-1].split(','), 1
        root = TreeNode(values[0])
        queue = [root]

        while queue:
            node = queue.pop(0)
            if values[i] != 'null':
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if values[i] != 'null':
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
