#! /usr/bin/env python
# coding: utf-8

# 给定两个用链表表示的整数，每个节点包含一个数位。 
# 
#  这些数位是反向存放的，也就是个位排在链表首部。 
# 
#  编写函数对这两个整数求和，并用链表形式返回结果。 
# 
#  
# 
#  示例： 
# 
#  输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
# 输出：2 -> 1 -> 9，即912
#  
# 
#  进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢? 
# 
#  示例： 
# 
#  输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
# 输出：9 -> 1 -> 2，即912
#  
#  Related Topics 链表 数学 
#  👍 65 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        cur = v = ListNode(0)

        while l1 and l2:
            carry, val = divmod(l1.val + l2.val + carry, 10)
            cur.next = ListNode(val)
            cur, l1, l2 = cur.next, l1.next, l2.next

        if l2:
            l1 = l2

        while l1:
            carry, val = divmod(l1.val + carry, 10)
            cur.next = ListNode(val)
            cur, l1 = cur.next, l1.next

        if carry:
            cur.next = ListNode(carry)

        return v.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
