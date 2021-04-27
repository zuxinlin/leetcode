#! /usr/bin/env python
# coding: utf-8

# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。 
# 
#  示例: 
# 
#  s = "abaccdeff"
# 返回 "b"
# 
# s = "" 
# 返回 " "
#  
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 50000 
#  Related Topics 哈希表 
#  👍 86 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        cache = {}

        for c in s:
            if c in cache:
                cache[c] += 1
            else:
                cache[c] = 1

        for c in s:
            if cache[c] == 1:
                return c

        return ' '

# leetcode submit region end(Prohibit modification and deletion)
