#! /usr/bin/env python
# coding: utf-8

# 编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。
# 分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。 
# 
#  示例: 
# 
#  输入: head = 3->5->8->5->10->2->1, x = 5
# 输出: 3->1->2->10->5->5->8
#  
#  Related Topics 链表 双指针 
#  👍 58 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
