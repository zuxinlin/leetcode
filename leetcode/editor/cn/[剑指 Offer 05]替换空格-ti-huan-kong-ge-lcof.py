#! /usr/bin/env python
# coding: utf-8

# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We%20are%20happy." 
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 10000 
#  👍 98 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''

        for c in s:
            if c == ' ':
                c = '%20'

            result += c

        return result
# leetcode submit region end(Prohibit modification and deletion)
