#! /usr/bin/env python
# coding: utf-8

# 给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。 
# 
#  请你将 list1 中第 a 个节点到第 b 个节点删除，并将list2 接在被删除节点的位置。 
# 
#  下图中蓝色边和节点展示了操作后的结果： 
# 
#  请你返回结果链表的头指针。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# 输出：[0,1,2,1000000,1000001,1000002,5]
# 解释：我们删除 list1 中第三和第四个节点，并将 list2 接在该位置。上图中蓝色的边和节点为答案链表。
#  
# 
#  示例 2： 
# 
#  
# 输入：list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,100
# 0003,1000004]
# 输出：[0,1,1000000,1000001,1000002,1000003,1000004,6]
# 解释：上图中蓝色的边和节点为答案链表。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= list1.length <= 104 
#  1 <= a <= b < list1.length - 1 
#  1 <= list2.length <= 104 
#  
#  Related Topics 链表 
#  👍 12 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """

# leetcode submit region end(Prohibit modification and deletion)
