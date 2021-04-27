#
# 
# @param s string字符串 
# @return bool布尔型
#
class Solution:
    def checkValidString(self, s):
        # write code here
        if not s:
            return True

        stack = []
        for c in s:
            if c in ['(', '*']:
                stack.append(c)
            elif c == ')':
                data = stack.pop()

                if data not in ['(', '*']:
                    return False

        return not stack


if __name__ == '__main__':
    solution = Solution()
    assert solution.checkValidString('(((*())()*')
