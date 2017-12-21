#! /usr/env python
# coding: utf-8
'''
Maximum Binary Tree
'''


class TreeNode(object):
    """
    树节点类
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
    Construct the maximum tree by the given array and output the root node of this tree.

    Example 1:
    Input: [3,2,1,6,0,5]
    Output: return the tree root node representing the following tree:

    Note:
    The size of the given array will be in the range [1,1000].
    """

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        # if not nums:
        #     return None

        # max_index, max_data = 0, nums[0]

        # for index, value in enumerate(nums):
        #     if value > max_data:
        #         max_data = value
        #         max_index = index

        # node = TreeNode(max_data)
        # node.left = self.constructMaximumBinaryTree(nums[:max_index])
        # node.right = self.constructMaximumBinaryTree(nums[max_index + 1:])

        # return node

        stack = []

        for num in nums:
            new_node = TreeNode(num)

            while stack and stack[-1].val < num:
                new_node.left = stack.pop()

            if stack:
                stack[-1].right = new_node

            stack.append(new_node)

        return stack[0]

    def first(self, root):
        """
        前序遍历
        """

        if not root:
            return

        print root.val, '->',
        self.first(root.left)
        self.first(root.right)

    def level(self, root):
        """
        层次遍历
        """

        queue = [root]

        while queue:
            current = queue.pop(0)
            print current.val, '->',

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)


def main():
    """
    main函数
    """

    solution = Solution()
    root = solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    # 前序遍历
    solution.first(root)
    print

    # 层次遍历
    solution.level(root)


if __name__ == '__main__':
    main()
