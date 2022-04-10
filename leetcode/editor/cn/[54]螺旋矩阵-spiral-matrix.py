#!/bin/env python
# coding: utf-8

# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
#  Related Topics 数组 
#  👍 765 👎 0


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


if __name__ == '__main__':
    solution = Solution()
