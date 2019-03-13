#! /usr/bin/env python
# coding: utf-8

'''
题目： 盛最多水的容器 https://leetcode-cn.com/problems/container-with-most-water/
主题： array & two pointers

解题思路：
1. 头尾双指针，从相距最远的两个点开始，先算出面积；左边高度低，左边前进一步，反之右边后退一步；
'''


class Solution(object):
    '''
    '''

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # 从相距最远的两个点开始，先算出面积
        # 如果左边高度比右边小，那就左边往右挪，并且计算面积和当前面积比较
        # 如果右边高度比左边小，那就从右往左挪，并且计算面积和当前面积比较
        max_area, l, r = 0, 0, len(height) - 1

        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


if __name__ == '__main__':
    solution = Solution()
    height = [4, 2, 1, 5]
    print solution.maxArea(height)
