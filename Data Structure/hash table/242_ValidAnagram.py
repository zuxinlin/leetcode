# coding: utf-8

'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 统计字符串字母个数
        # l = 'abcdefghijklmnopqrstuvwxyz'
        # for i in l:
        #     if(s.count(i) != t.count(i)):
        #         return False
        # return True 

        # 通过哈希表统计比较
        first = {}
        second = {}

        for i in s:
            first[i] = (first[i] + 1) if i in first else 1

        for i in t:
            second[i] = (second[i] + 1) if i in second else 1

        if len(first.keys()) < len(second.keys()):
            first, second = second, first

        for key in first:
            if key not in second or first[key] != second[key]:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    assert solution.isAnagram('anagram', 'nagaram')
    assert solution.isAnagram('rat', 'car') is False