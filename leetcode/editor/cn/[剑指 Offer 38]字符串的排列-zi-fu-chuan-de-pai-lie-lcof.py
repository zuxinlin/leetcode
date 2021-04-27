#! /usr/bin/env python
# coding: utf-8

# 输入一个字符串，打印出该字符串中字符的所有排列。 
# 
#  
# 
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 
# 
#  
# 
#  示例: 
# 
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  
# 
#  
# 
#  限制： 
# 
#  1 <= s 的长度 <= 8 
#  Related Topics 回溯算法 
#  👍 254 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        data = list(s)

        def backtrack(path, depth):
            if depth == len(data):
                result.append(''.join(data))
                return
            dic = set()
            for i in range(depth, len(data)):
                if data[i] in dic:
                    continue  # 重复，因此剪枝
                dic.add(data[i])
                data[depth], data[i] = data[i], data[depth]
                backtrack(path, depth + 1)
                data[depth], data[i] = data[i], data[depth]

        backtrack([], 0)
        return result


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation('abc'))
