#! /usr/bin/env python
# coding: utf-8

# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 564 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(path, begin=1):
            # 满足结束条件，结果必须深拷贝
            if len(path) == k:
                result.append(list(path))
                return

            # 遍历所有选择，剪枝减少计算量
            for num in range(begin, n - (k - len(path)) + 2):
                path.append(num)
                backtrack(path, num + 1)
                path.pop()

        backtrack([])

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
# leetcode submit region end(Prohibit modification and deletion)
