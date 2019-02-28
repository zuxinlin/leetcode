#! /usr/bin/env python
# coding: utf-8

class ListNode(object):
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    '''
    Given a linked list, remove the n-th node from the end of list and return its head.

    Example:
    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:
    Given n will always be valid.

    Follow up:
    Could you do this in one pass?

    主题：linked list & two pointers
    题目：删除单链表倒数第N个节点

    解题思路：
    方法1：采用双指针，第二个指针先走N步，然后一起走，直到第二个节点到尾节点，删除第一个节点
    '''

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # 只有一个节点
        if head.next == None:
            return None
        
        first, second = head, head
        index = 0

        while index < n and second:
            second = second.next
            index += 1

        # 倒数第N个元素在第一个
        if second is None:
            return head.next

        while second.next:
            first = first.next
            second = second.next

        # 删除该节点
        first.next = first.next.next

        return head

    def createLinkedList(self, list):
        '''
        创建单链表
        '''

        root = current = ListNode(0)

        for i in list:
            current.next = ListNode(i)
            current = current.next

        return root.next

    def traverse(self, root):
        '''
        遍历单链表
        '''

        current = root

        while current:
            print current.val, '->' if current.next != None else '',
            current = current.next

if __name__ == '__main__':
    solution = Solution()
    print solution.fourSum([1, 0, -1, 0, -2, 2], 0)
