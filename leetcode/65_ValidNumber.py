#! /usr/bin/env python
# coding: utf-8
'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
'''


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        try:
            float(s)

            return True
        except:
            return False


if __name__ == '__main__':
    solution = Solution()
    list = ["0", " 0.1 ", "abc", "1 a", "2e10", "+ 1"]

    for i in list:
        print solution.isNumber(i)
