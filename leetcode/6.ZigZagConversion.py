# coding: utf-8

'''
题目： Z 字形变换 https://leetcode-cn.com/problems/zigzag-conversion/
主题： string

解题思路：
1. 按照z字形走向进行遍历字符串，存储到数组
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # 边界条件
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x

            if index == 0:
                # 第一行开始，从上往下，步数是1
                step = 1
            elif index == numRows -1:
                # 到最后一行，就要从下晚上，步数是-1
                step = -1

            index += step

        return ''.join(L)


if __name__ == '__main__':
    solution = Solution()
    assert solution.convert('LEETCODEISHIRING', 3) == 'LCIRETOESIIGEDHN'
    assert solution.convert('LEETCODEISHIRING', 4) == 'LDREOEIIECIHNTSG'
