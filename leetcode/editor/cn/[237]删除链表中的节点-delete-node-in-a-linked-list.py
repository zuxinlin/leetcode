#! /usr/bin/env python
# coding: utf-8

# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。 
# 
#  
# 
#  现有一个链表 -- head = [4,5,1,9]，它可以表示为: 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [4,5,1,9], node = 5
# 输出：[4,1,9]
# 解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
#  
# 
#  示例 2： 
# 
#  输入：head = [4,5,1,9], node = 1
# 输出：[4,5,9]
# 解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表至少包含两个节点。 
#  链表中所有节点的值都是唯一的。 
#  给定的节点为非末尾节点并且一定是链表中的一个有效节点。 
#  不要从你的函数中返回任何结果。 
#  
#  Related Topics 链表 
#  👍 891 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre, cur = node, node.next

        while cur.next:
            pre.val = cur.val
            pre, cur = pre.next, cur.next

        pre.val = cur.val
        pre.next = None


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
