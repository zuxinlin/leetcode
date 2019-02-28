#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    '''
    Given a linked list, determine if it has a cycle in it.

    To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

    Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

    Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

    Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

    Follow up:
    Can you solve it using O(1) (i.e. constant) memory?

    主题：array & two pointers
    题目：从数组中移除重复元素

    解题思路：
    1. 双头指针，分为快慢。如果最终快指针和慢指针相遇，则有环。否则没有；
    '''

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
