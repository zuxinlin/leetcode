#! /usr/bin/env python
# coding: utf-8

'''
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        add = 0
        result = []
        is_first = True

        for i in digits[::-1]:
            if is_first:
                i += 1
                is_first = False
            add, temp = divmod(i + add, 10)
            result.append(temp)

        if add > 0:
            result.append(add)

        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
    assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
