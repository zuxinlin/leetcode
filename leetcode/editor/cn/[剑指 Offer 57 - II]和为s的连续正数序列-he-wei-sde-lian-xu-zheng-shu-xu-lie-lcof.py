#! /usr/bin/env python
# coding: utf-8

# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。 
# 
#  序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = 9
# 输出：[[2,3,4],[4,5]]
#  
# 
#  示例 2： 
# 
#  输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= target <= 10^5 
#  
# 
#  
#  👍 253 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        # 双指针滑动窗口
        left, right, result = 1, 2, []

        while left < right:
            sum = (left + right) * (right - left + 1) / 2

            if sum == target:
                result.append([i for i in range(left, right + 1)])
                left += 1
                right += 1
            elif sum < target:
                right += 1
            else:
                left += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    solution.findContinuousSequence(9)
# leetcode submit region end(Prohibit modification and deletion)
