# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# reverse the given linked list
# @param head ListNode类 the head of the linked list
# @param n int整型 the N
# @return ListNode类
#
'''
给一个单向链表以及整数N，使得每N个元素为一组进行翻转。要求时间复杂度O(n), 空间复杂度O(1)。
'''


class Solution:
    def reverseLinkedList(self, head, n):
        if not head:
            return

        def reverse(first, second):
            pre, cur = None, first

            while cur and cur != second:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp

            return pre

        first, second = head, head
        i = 0

        while second and i < n:
            second = second.next
            i += 1

        node = reverse(first, second)
        first.next = self.reverseLinkedList(second, n)

        return node

# write code here
