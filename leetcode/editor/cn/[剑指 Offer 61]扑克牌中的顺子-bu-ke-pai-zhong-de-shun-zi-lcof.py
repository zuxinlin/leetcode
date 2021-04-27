#! /usr/bin/env python
# coding: utf-8

# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任
# 意数字。A 不能视为 14。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5]
# 输出: True 
# 
#  
# 
#  示例 2: 
# 
#  输入: [0,0,1,2,5]
# 输出: True 
# 
#  
# 
#  限制： 
# 
#  数组长度为 5 
# 
#  数组的数取值为 [0, 13] . 
#  👍 120 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums.sort()
        # joker = nums.count(0)
        #
        # for i in range(1, 5):
        #     if nums[i - 1] > 0:
        #         if nums[i] - nums[i - 1] == 0 or nums[i] - nums[
        #             i - 1] > joker + 1:
        #             return False
        #         else:
        #             joker -= nums[i] - nums[i - 1] - 1
        #
        # return True
        repeat = set()
        ma, mi = 0, 14

        for num in nums:
            if num == 0:
                continue  # 跳过大小王

            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌

            if num in repeat:
                return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


if __name__ == '__main__':
    solution = Solution()
    solution.isStraight([0, 0, 1, 2, 5])
# leetcode submit region end(Prohibit modification and deletion)
