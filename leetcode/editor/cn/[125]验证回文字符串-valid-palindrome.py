#! /usr/bin/env python
# coding: utf-8

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串 
#  👍 372 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 边界条件
        if not s or len(s) <= 1:
            return True

        # 预处理，过滤无关字符
        s = [c.lower() for c in s if c.isalnum()]
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
