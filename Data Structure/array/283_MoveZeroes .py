# coding: utf-8

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be
[1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # 不开辟新空间，把0都挪动数组末尾，保证原来数字的顺序
        # 
        zero = 0

        for i in xrange(len(nums)):
            if nums[i] != 0:
                if i != zero:
                    nums[zero], nums[i] = nums[i], nums[zero]

                zero += 1

        return nums


if __name__ == '__main__':
    solution = Solution()
    assert [1, 3, 12, 0, 0] == solution.moveZeroes([0, 1, 0, 3, 12])
