# coding: utf-8

'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        cache = {}

        # 先用哈希表存储一个数组统计情况，另外一个数组查表即可
        for i in nums1:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1

        for i in nums2:
            if i in cache and cache[i] > 0:
                result.append(i)
                cache[i] -= 1

        return result

if __name__ == '__main__':
    solution = Solution()
    assert solution.intersect([1, 2, 2, 1], [2]) == [2,]
    assert solution.intersect([3,1,2], [1, 1]) == [1,]