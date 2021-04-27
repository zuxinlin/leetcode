#! /usr/bin/env python
# coding: utf-8

# 实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。 
# 
#  
# 
#  示例： 
# 
#  输入：单向链表a->b->c->d->e->f中的节点c
# 结果：不返回任何数据，但该链表变为a->b->d->e->f
#  
#  Related Topics 链表 
#  👍 98 👎 0


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
        pre, cur = None, node

        # 遍历拷贝值。cur到最后一个节点，然后删除最后一个节点
        while cur.next:
            cur.val = cur.next.val
            pre, cur = cur, cur.next

        pre.next = None


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
