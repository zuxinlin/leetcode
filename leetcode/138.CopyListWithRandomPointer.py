#! /usr/bin/env python
# coding: utf-8

import collections

'''
题目： 带随机指针链表拷贝 https://leetcode.com/problems/copy-list-with-random-pointer/
主题： hash table & linked list

解题思路：
1. 采用字典存储
'''


class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        current = head
        node_map = collections.defaultdict(lambda *args: Node(0, None, None))
        node_map[None] = None

        while current:
            node_map[current].val = current.val
            node_map[current].next = node_map[current.next]
            node_map[current].random = node_map[current.random]
            current = current.next

        return node_map[head]


if __name__ == '__main__':
    solution = Solution()
    a, b, nums = 1, 2, [1, 2, 1]
    print [b, a], [nums.count(a) > len(nums)//2], [b, a][nums.count(a) > len(nums)//2]