'''
给定一个字符串式子，返回它的计算结果。算术规则为: k*[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
注意 k 保证为正整数。e.g. s = "3*[a2*[c]]", 返回 “accaccacc”
'''


class Solution(object):
    def computeString(self, s):
        stack = []
        num = 0
        res = ""
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == '*':
                continue
            elif i == "[":
                stack.append((res, num))
                res, num = "", 0
            elif i == "]":
                top = stack.pop()
                res = top[0] + res * top[1]
            else:
                res += i

        return res
