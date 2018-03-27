#! /usr/bin/env python
# coding: utf-8
"""
Delete Node in a Linked List
"""


class ListNode(object):
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    '''
    Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

    Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
    '''

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
    print solution.addTwoNumbers(l1, l2)
