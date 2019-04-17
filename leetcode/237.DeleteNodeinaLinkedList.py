#! /usr/bin/env python
# coding: utf-8


'''
题目： 单链表中删除一个节点 https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
主题： linked list

解题思路：

'''


class ListNode(object):
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next

    def createLinkedList(self, list):
        root = current = ListNode(0)

        for i in list:
            current.next = ListNode(i)
            current = current.next

        return root.next


if __name__ == '__main__':
    solution = Solution()
    l1 = solution.createLinkedList([2, 4, 3])
    l2 = solution.createLinkedList([5, 6, 4])
