#!/bin/env python
# coding: utf-8

# 给你一个整数数组 nums，请你将该数组升序排列。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 50000 
#  -50000 <= nums[i] <= 50000 
#  
#  👍 280 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def quick_sort(self, arr, low, high):
        """
        快速排序(不稳定，时间复杂度nlogn)，分治法解决
        """

        def partition(arr, l, r):
            pivot = random.randint(l, r)
            arr[pivot], arr[r] = arr[r], arr[pivot]
            i = l - 1

            for j in range(l, r):
                if arr[j] < arr[r]:
                    i += 1
                    arr[j], arr[i] = arr[i], arr[j]

            i += 1
            arr[i], arr[r] = arr[r], arr[i]
            return i

        if low < high:
            pivot = partition(arr, low, high)
            self.quick_sort(arr, low, pivot - 1)
            self.quick_sort(arr, pivot + 1, high)

    def merge_sort(self, arr, low, high):
        """
        归并排序(稳定，时间复杂度nlogn，空间复杂度n)，分治法解决；
        把数组拆成两个数组，分别排序，然后合并起来
        """

        def merge(arr, low, mid, high):
            """
            合并两个有序数组，先从头遍历两个数组小的元素，遍历完一个数组后，把另外一个全插入新数组
            """

            tmp = []
            i, j = low, mid + 1

            while i <= mid and j <= high:
                if arr[i] <= arr[j]:
                    tmp.append(arr[i])
                    i += 1
                else:
                    tmp.append(arr[j])
                    j += 1

            while i <= mid:
                tmp.append(arr[i])
                i += 1

            while j <= high:
                tmp.append(arr[j])
                j += 1

            for i in range(len(tmp)):
                arr[low + i] = tmp[i]

        if low < high:
            mid = (low + high) // 2
            self.merge_sort(arr, low, mid)
            self.merge_sort(arr, mid + 1, high)

            return merge(arr, low, mid, high)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # self.quick_sort(nums, 0, len(nums) - 1)
        self.merge_sort(nums, 0, len(nums) - 1)

        return nums


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    solution.sortArray([5, 2, 3, 1])
