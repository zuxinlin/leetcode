#! /usr/bin/env python
# coding: utf-8

# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。 
# 
#  注意：本题相对原题稍作改动 
# 
#  示例： 
# 
#  输入： 1->2->3->4->5 和 k = 2
# 输出： 4 
# 
#  说明： 
# 
#  给定的 k 保证是有效的。 
#  Related Topics 链表 双指针 
#  👍 67 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        if not head or k <= 0:
            return head.val

        pre, cur, count = head, head, 0

        while cur and count < k:
            cur = cur.next
            count += 1

        # 链表长度小于k 直接返回
        if not cur and count != k:
            return

        while cur:
            pre, cur = pre.next, cur.next

        return pre.val


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
