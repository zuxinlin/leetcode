# coding: utf-8

'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)
        source_len = len(haystack)
        target_len = len(needle)

        for i in range(source_len - target_len + 1):
            if haystack[i:i+target_len] == needle:
                return i
            
        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.strStr('hello', 'll') == 2
