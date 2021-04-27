#! /usr/bin/env python
# coding: utf-8

# 编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。 
# 
#  示例1: 
# 
#  
#  输入：[1, 2, 3, 3, 2, 1]
#  输出：[1, 2, 3]
#  
# 
#  示例2: 
# 
#  
#  输入：[1, 1, 1, 1, 2]
#  输出：[1, 2]
#  
# 
#  提示： 
# 
#  
#  链表长度在[0, 20000]范围内。 
#  链表元素在[0, 20000]范围内。 
#  
# 
#  进阶： 
# 
#  如果不得使用临时缓冲区，该怎么解决？ 
#  Related Topics 链表 
#  👍 101 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # 虚拟头结点
        s, cur, v = set(), head, ListNode(0)
        v.next = head
        pre = v

        while cur:
            if cur.val in s:
                pre.next = cur.next
                cur = cur.next
            else:
                s.add(cur.val)
                pre, cur = cur, cur.next

        return v.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
