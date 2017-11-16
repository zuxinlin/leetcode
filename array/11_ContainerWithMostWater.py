# coding: utf-8

'''
Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''


class Solution(object):
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
