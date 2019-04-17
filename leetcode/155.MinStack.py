
# coding: utf-8

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

from collections import deque


class Solution(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        return self.data.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.data)


if __name__ == '__main__':
    solution = Solution()
    assert solution.isValid("()")
    assert solution.isValid("()[]{}")
    assert solution.isValid("{[]}")
    assert not solution.isValid("(]")
    assert not solution.isValid("([)]")
