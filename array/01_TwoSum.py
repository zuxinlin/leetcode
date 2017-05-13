# coding: utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 边界条件判断
        if len(nums) <= 1:
            return False

        # 以空间换时间，用字典存储，key是第二个加数，value是第一个加数的下标
        buff_dict = {}

        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    assert [0, 1] == solution.twoSum(nums, target)
