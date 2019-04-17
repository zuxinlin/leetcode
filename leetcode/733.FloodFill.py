#! /usr/bin/env python
# coding: utf-8

'''
题目：图像渲染 https://leetcode-cn.com/problems/flood-fill/
主题：depth-first search

解题思路：
1. 深度优先遍历，往四个方向，注意边界条件

'''


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        R, C = len(image), len(image[0])
        color = image[sr][sc]

        if color == newColor:
            return image

        def dfs(r, c):
            # 和起点颜色一样的都要涂上
            if image[r][c] == color:
                image[r][c] = newColor

                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image


if __name__ == '__main__':
    solution = Solution()
