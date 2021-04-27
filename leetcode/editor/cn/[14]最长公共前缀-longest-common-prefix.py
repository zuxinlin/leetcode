#! /usr/bin/env python
# coding: utf-8

# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 仅由小写英文字母组成 
#  
#  Related Topics 字符串 
#  👍 1579 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        m, s, n = 0, len(strs[0]), len(strs)
        result = ''

        for i in range(1, n):
            c = len(strs[i])
            if c < s:
                m, s = i, c

        for i in range(s):
            flag = False
            for j in range(n):
                if strs[j][i] != strs[m][i]:
                    flag = True

            if flag:
                break
            else:
                result += strs[m][i]

        return result


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    solution.longestCommonPrefix(["flower", "flow", "flight"])
