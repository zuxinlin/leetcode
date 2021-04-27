#! /usr/bin/env python
# coding: utf-8

# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
#  Related Topics 数组 
#  👍 230 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 边界条件
        if not matrix or not matrix[0]:
            return list()

        # 一圈一圈访问
        top, left, bottom, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        result = []

        while left <= right and top <= bottom:
            # 上
            for column in range(left, right + 1):
                result.append(matrix[top][column])

            # 右
            for row in range(top + 1, bottom + 1):
                result.append(matrix[row][right])

            if left < right and top < bottom:
                # 下
                for column in range(right - 1, left, -1):
                    result.append(matrix[bottom][column])

                # 左
                for row in range(bottom, top, -1):
                    result.append(matrix[row][left])

            top += 1
            left += 1
            bottom -= 1
            right -= 1

        return result
# leetcode submit region end(Prohibit modification and deletion)
