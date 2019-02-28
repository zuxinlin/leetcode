#! /usr/bin/env python
# coding: utf-8

'''
题目： 链表两个非负整数相加 https://leetcode-cn.com/problems/add-two-numbers/
主题： linked list & math

解题思路：
1. 按照算法加法，两位以及进位相加
'''


class ListNode(object):
    '''
    链表节点定义
    '''

    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList(object):
    '''
    链表定义
    '''

    def __init__(self, list):
        '''
        创建单链表
        '''

        root = current = ListNode(0)

        for value in list:
            current.next = ListNode(value)
            current = current.next

        self.root = root.next

    def traverse(self, root=None):
        '''
        遍历单链表
        '''

        current = self.root if root is None else root

        while current:
            print current.val, '->' if current.next != None else '',
            current = current.next

        print


class Solution(object):
    '''
    '''

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 建立一个头部空节点
        root = current = ListNode(0)
        carry = 0

        # 只有当l1和l2和进位都为空的时候，循环才退出
        while l1 or l2 or carry:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, val = divmod(v1 + v2 + carry, 10)
            current.next = ListNode(val)
            current = current.next

        return root.next


if __name__ == '__main__':
    l1 = LinkedList([2, 4, 3])
    l2 = LinkedList([5, 6, 4])
    l1.traverse()
    l2.traverse()
    l1.traverse(Solution().addTwoNumbers(l1.root, l2.root))
