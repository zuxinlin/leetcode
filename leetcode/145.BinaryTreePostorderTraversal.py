#! /usr/bin/env python
# coding: utf-8

'''
题目： 二叉树后序遍历 https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
主题： stack & tree

解题思路：
1. 深度优先遍历，左 右 根
'''


class Solution(object):
    def postorder(self, root, result):
        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(root.val)

    def postorder_stack(self, root):
        if root:
            stack = []
            result = []
            current = root
            pre = None

            while current or stack:
                if current:
                    stack.append(current)
                    current = current.left
                else:
                    peek = stack[-1]

                    # 如果当前栈顶元素的右结点存在并且还没访问过（也就是右结点不等于上一个访问结点），那么就把当前结点移到右结点继续循环
                    if peek.right and pre != peek.right:
                        current = peek.right
                    else:
                        stack.pop()
                        result.append(peek.val)
                        pre = peek

            return result

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        self.postorder(root, result)

        return result
        # return self.postorder_stack(root)


if __name__ == '__main__':
    pass
