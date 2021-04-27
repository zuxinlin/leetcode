#! /usr/bin/env python
# coding: utf-8

# 给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。 
# 
#  如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的
# 位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。 
# 
#  
# 
#  进阶： 
# 
#  
#  你是否可以不用额外空间解决此题？ 
#  
# 
#  
#  Related Topics 链表 
#  👍 68 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 用set存储访问过的节点
        s, cur = set(), head

        while cur:
            if cur not in s:
                s.add(cur)
                cur = cur.next
            else:
                return cur


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
