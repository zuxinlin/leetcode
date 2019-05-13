#! /usr/bin/env python
# coding: utf-8
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

class ListNode(object):
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        data = []
        current = self

        while current != None:
            data.append(str(current.val))
            current = current.next

        return ' -> '.join(data)

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 建立一个空头结点
        current = dummy = ListNode(0)

        # 当l1和l2都不为空时，比较两者的值
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
                
            current = current.next

        current.next = l1 or l2

        return dummy.next

    def createLinkedList(self, list):
        current = root = ListNode(0)

        for i in list:
            current.next = ListNode(i)
            current = current.next

        return root.next


if __name__ == '__main__':
    solution = Solution()
    l1 = solution.createLinkedList([2, 3, 4])
    l2 = solution.createLinkedList([1, 3, 5])
    print solution.mergeTwoLists(l1, l2)
