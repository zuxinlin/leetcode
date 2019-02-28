# coding: utf-8

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

from collections import deque


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 边界条件判断
        if s == None or len(s) == 0:
            return True

        if len(s) == 1:
            return False

        # 如果是下面三种情况，需要出栈，其他入栈，最后看栈是否为空
        cache = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        queue = []
        queue.append(s[0])

        for element in s[1:]:
            if len(queue) > 0 and cache.has_key(element) and queue[-1] == cache[element]:
                queue.pop()
            else:
                queue.append(element)

        return len(queue) == 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.isValid("()")
    assert solution.isValid("()[]{}")
    assert solution.isValid("{[]}")
    assert not solution.isValid("(]")
    assert not solution.isValid("([)]")
