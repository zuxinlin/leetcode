#! /usr/bin/env python
# coding: utf-8

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 1306 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(nums, path, depth=0):
            # 满足结束条件，结果必须深拷贝
            if depth == len(nums):
                result.append(list(path))
                return

            # 遍历所有选择
            for num in nums:
                # 剪枝
                if num not in path:
                    path.append(num)
                    backtrack(nums, path, depth + 1)
                    path.pop()

        backtrack(nums, [])

        return result
# leetcode submit region end(Prohibit modification and deletion)
