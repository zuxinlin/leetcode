#! /usr/bin/env python
# coding: utf-8

'''
题目：求数组三个数相加等于0的所有可能组合
主题：array & two pointers

解题思路：
方法1：采用排序加双指针的方式来
方法2：采用排序加哈希表的方式来，类似2sum，a + b + c = 0 => a = -b - c
'''


class Solution(object):
    def threeSumByTwoPointers(self, nums):
        # 边界条件判断
        if len(nums) < 3:
            return []

        nums.sort()
        result = []

        for (i, num) in enumerate(nums):
            # 过滤相同数据
            if i > 0 and num == nums[i-1]:
                continue

            # 头尾双指针
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = num + nums[left] + nums[right]

                if sum == 0:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 排除相同的数字组合
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum > 0:
                    right -= 1

                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                else:
                    left += 1

                    while left < right and nums[left-1] == nums[left]:
                        left += 1

        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []

        nums.sort()
        res = set()

        for i, target in enumerate(nums[:-2]):
            # 相同的值，直接过掉，避免重复
            if i > 0 and target == nums[i - 1]:
                continue

            # key是第二个加数，如果后续元素在字典内，说明加数和被加数都在数组中
            d = {}

            for first in nums[i+1:]:
                if first not in d:
                    d[-target-first] = 1
                else:
                    res.add((target, -target-first, first))

        return map(list, res)


if __name__ == '__main__':
    solution = Solution()
    print solution.threeSum([-1, 0, 1, 2, -1, -4])
