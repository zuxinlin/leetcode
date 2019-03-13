#! /usr/bin/env python
# coding: utf-8

'''
题目： 宝石与石头 https://leetcode-cn.com/problems/jewels-and-stones/
主题： hash table

解题思路：
1. 遍历S字符串，每个字符看是否在J中，有就加1
2. hash存储统计
'''


class Solution(object):
    '''
    '''

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # 字符串遍历
        # count = 0
        # 
        # for s in S:
        #     if s in J:
        #         count += 1

        # return count

        dict = {}
        result = 0

        for c in S:
            dict[c] = dict[c] + 1 if dict.has_key(c) else 1

        for c in J:
            if dict.has_key(c):
                result += dict[c]

        return result


if __name__ == '__main__':
    solution = Solution()
    assert 3 == solution.numJewelsInStones(J="aA", S="aAAbbbb")
    assert 0 == solution.numJewelsInStones(J="z", S="ZZ")
