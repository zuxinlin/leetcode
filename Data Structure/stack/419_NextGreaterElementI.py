# coding: utf-8

'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
'''


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        # 采用hash表和stack来做, 栈顶总是当前最小的元素
        hash = {}
        stack = []

        for x in nums:
            while stack and stack[-1] < x:
                hash[stack.pop()] = x

            stack.append(x)

        return map(lambda item: hash.get(item, -1), findNums)

        # cache = {}
        # count = len(nums)
        #
        # for i in xrange(count):
        #     isHave = False
        #
        #     for j in xrange(i + 1, count):
        #         if nums[j] > nums[i]:
        #             cache[nums[i]] = nums[j]
        #             isHave = True
        #             break
        #
        #     if not isHave:
        #         cache[nums[i]] = -1
        #
        # return map(lambda item: cache[item], findNums)


if __name__ == '__main__':
    solution = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert [-1, 3, -1] == solution.nextGreaterElement(nums1, nums2)
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    assert [3,-1] == solution.nextGreaterElement(nums1, nums2)
