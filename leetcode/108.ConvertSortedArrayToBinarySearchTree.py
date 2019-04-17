#! /usr/bin/env python
# coding: utf-8

'''
题目： 把有序数组转化成二叉搜索树 https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
主题： tree & depth-first search

解题思路：
1. 深度优先
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


if __name__ == '__main__':
    pass
