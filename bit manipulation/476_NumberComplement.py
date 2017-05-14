# coding: utf-8

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        return num ^ (2 ** (len(bin(num)) - 2) - 1)
        # i = 1
        #
        # while i <= num:
        #     i <<= 1
        #
        # return (i - 1) ^ num


if __name__ == '__main__':
    solution = Solution()
    assert 2 == solution.findComplement(5)
    assert 0 == solution.findComplement(1)
