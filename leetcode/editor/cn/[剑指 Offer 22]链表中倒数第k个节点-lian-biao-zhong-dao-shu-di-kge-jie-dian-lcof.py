#! /usr/bin/env python
# coding: utf-8

# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。 
# 
#  例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。 
# 
#  
# 
#  示例： 
# 
#  
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
# 
# 返回链表 4->5. 
#  Related Topics 链表 双指针 
#  👍 179 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or k <= 0:
            return None

        pre, cur, count = head, head, 0

        # 前面节点先走k步
        while cur and count < k:
            cur = cur.next
            count += 1

        if not cur and count != k:
            return None

        while cur:
            pre, cur = pre.next, cur.next

        return pre

# leetcode submit region end(Prohibit modification and deletion)
