#! /usr/bin/env python
# coding: utf-8

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  示例 4: 
# 
#  
# 输入: s = ""
# 输出: 0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s 由英文字母、数字、符号和空格组成 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 5338 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 滑动窗口
        window = set()
        r, n, result = 0, len(s), 0

        for i in range(n):
            # 窗口收缩一个
            if i != 0:
                window.remove(s[i - 1])

            # 窗口往右滑动
            while r < n and s[r] not in window:
                window.add(s[r])
                r += 1

            result = max(result, r - i)

        return result


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    solution = Solution()
    solution.lengthOfLongestSubstring('abcabcbb')
