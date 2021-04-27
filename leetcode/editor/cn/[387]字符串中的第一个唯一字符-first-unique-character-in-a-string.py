#! /usr/bin/env python
# coding: utf-8

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  
# 
#  示例： 
# 
#  s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
#  
# 
#  
# 
#  提示：你可以假定该字符串只包含小写字母。 
#  Related Topics 哈希表 字符串 
#  👍 377 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        result = float('inf')

        # 利用hash统计，存储次数和下标
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [1, i]
            else:
                d[c][0] += 1
                d[c][1] = i

        for c in d:
            if d[c][0] == 1:
                result = min(result, d[c][1])

        return result if result != float('inf') else -1


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
