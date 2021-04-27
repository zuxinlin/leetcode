#! /usr/bin/env python
# coding: utf-8

# 编写一个函数，检查输入的链表是否是回文的。 
# 
#  
# 
#  示例 1： 
# 
#  输入： 1->2
# 输出： false 
#  
# 
#  示例 2： 
# 
#  输入： 1->2->2->1
# 输出： true 
#  
# 
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 
#  👍 58 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result, cur = [], head

        while cur:
            result.append(cur.val)
            cur = cur.next

        return result == result[::-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
