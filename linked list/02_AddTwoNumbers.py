# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = current = ListNode(0)
        carry = 0

        # 只有当l1和l2和进位都为空的时候，循环才退出
        while l1 or l2 or carry:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, val = divmod(v1 + v2 + carry, 10)
            current.next = ListNode(val)
            current = current.next

        return root.next

    def createLinkedList(self, list):
        root = current = ListNode(0)

        for i in list:
            current.next = ListNode(i)
            current = current.next

        return root.next


if __name__ == '__main__':
    solution = Solution()
    l1 = solution.createLinkedList([2, 4, 3])
    l2 = solution.createLinkedList([5, 6, 4])
    print solution.addTwoNumbers(l1, l2)
    # assert [0, 1] == solution.twoSum(nums, target)
