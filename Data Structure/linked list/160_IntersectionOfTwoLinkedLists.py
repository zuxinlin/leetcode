#! /usr/bin/env python
# coding: utf-8
'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
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
    def get_length(self, node):
        count = 0
        while node is not None:
            node = node.next
            count += 1

        retur count

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if not headA or not headB:
            return None

        a_length = self.get_length(headA)
        b_length = self.get_length(headB)

        if a_length < b_length:
            headA, headB = headB, headA
            a_length, b_length = b_length, a_length

        for _ in range(a_length - b_length):
            headA = headA.next

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None




if __name__ == '__main__':
    solution = Solution()
    l1 = solution.createLinkedList([2, 3, 4])
    l2 = solution.createLinkedList([1, 3, 5])
    print solution.mergeTwoLists(l1, l2)
