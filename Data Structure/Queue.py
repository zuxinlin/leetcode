#! /usr/bin/env python
# coding: utf - 8


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.in_2_out()

        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.in_2_out()

        return self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def in_2_out(self):
        # 只有出的栈为空时候，才把入栈的数据往里面挪动
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
