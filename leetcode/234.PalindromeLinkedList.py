#! /usr/bin/env python
# coding: utf-8

'''
题目： 回文链表 
主题： linked list & two pointers

解题思路：
1. 快慢指针，还有一个反转指针，走到中间，然后开始对比；
'''


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
            
        return not rev


if __name__ == '__main__':
    solution = Solution()