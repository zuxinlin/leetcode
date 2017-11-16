# coding: utf-8

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity
should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # 两个数组合并然后排序，然后看数组大小是奇数还是偶数
        # 奇数的话就是中间的那个，偶数中间两个求平均数
        nums = nums1 + nums2
        nums.sort()
        m = len(nums) / 2
        mm = len(nums) % 2

        if mm > 0:
            return nums[m]
        else:
            return (nums[m - 1] + nums[m]) / 2.0


if __name__ == '__main__':
    solution = Solution()
    nums1 = [2, 1, 6]
    nums2 = [4, 3, 5]
    assert 3.5 == solution.findMedianSortedArrays(nums1, nums2)
