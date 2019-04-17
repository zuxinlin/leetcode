#! /usr/bin/env python
# coding: utf-8

'''
题目： 反转链表 https://leetcode-cn.com/problems/reverse-linked-list/
主题： linked list

解题思路：
1. 链表指针反转
'''


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre = None
        current = head

        while current:
            next = current.next
            current.next = pre
            pre = current
            current = next

        return pre

if __name__ == '__main__':
    solution = Solution()
    