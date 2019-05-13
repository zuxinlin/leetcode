#! /usr/bin/env python
# coding: utf-8

'''
题目： 排序列表 https://leetcode-cn.com/problems/sort-list/
主题： linked list & sort

解题思路：
1. 归并排序或者快排
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head

        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None

        def merge(h1, h2):
            dummy = tail = ListNode(None)

            while h1 and h2:
                if h1.val < h2.val:
                    tail.next, tail, h1 = h1, h1, h1.next
                else:
                    tail.next, tail, h2 = h2, h2, h2.next

            tail.next = h1 or h2

            return dummy.next

        return merge(*map(self.sortList, (head, slow)))


if __name__ == '__main__':
    pass
