#! /usr/bin/env python
# coding: utf-8

# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [1,3,2]
# 输出：[2,3,1] 
# 
#  
# 
#  限制： 
# 
#  0 <= 链表长度 <= 10000 
#  Related Topics 链表 
#  👍 135 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # 顺序访问链表，结果存储到数组，再逆序数组结果
        current = head
        result = []

        while current:
            result.append(current.val)
            current = current.next

        return result[::-1]
# leetcode submit region end(Prohibit modification and deletion)
