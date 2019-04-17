#! /usr/bin/env python
# coding: utf-8

'''
题目：求数组四个数相加等于target的组合
主题：array & hash table & two pointers

解题思路：
方法1：采用排序加双指针的方式来，采用递归方式
'''


class Solution(object):
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            # early termination
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
                return

            if N == 2:
                # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1

                        # 避免相同的元素
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target - nums[i], N-1,
                                 result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)

        return results


if __name__ == '__main__':
    solution = Solution()
    print solution.fourSum([1, 0, -1, 0, -2, 2], 0)
