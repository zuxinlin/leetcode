#! /usr/bin/env python
# coding: utf-8

'''
题目： 逆波兰表达式 https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
主题： stack

解题思路：
1. 使用栈，遇到操作符，弹出两个数，否则进栈
'''


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = set(["+", "-", "*", "/"])

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()

                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in
                    # Leetcode it should return 0
                    stack.append(abs(l) // abs(r) * (-1 if l * r < 0 else 1))

        return stack[0]


if __name__ == '__main__':
    solution = Solution()
    assert 9 == solution.evalRPN(["2", "1", "+", "3", "*"])
    assert 6 == solution.evalRPN(["4", "13", "5", "/", "+"])
    assert 22 == solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
