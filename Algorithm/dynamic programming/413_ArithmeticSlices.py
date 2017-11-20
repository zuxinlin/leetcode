# coding: utf-8

'''
A sequence of number is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.
1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any
pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.
'''


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # 找连续等差数列,一个长度为n的等差数列，设m=n-2，则包括子数列在内，
        # 一共可以组成m*(1+m)/2个长度大于3的等差数列，简单的数列求和
        l = len(A)

        if l < 3:
            return 0

        # cur, sum = 0, 0
        #
        # for i in xrange(1, l - 1):
        #     if A[i] - A[i - 1] == A[i + 1] - A[i]:
        #         cur += 1
        #         sum += cur
        #     else:
        #         cur = 0
        #
        # return sum

        # 定义一个一维dp数组，其中dp[i]表示，到i位置为止的算数切片的个数
        dp = [0] * l
        res = 0

        for i in xrange(2, l):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1

            res += dp[i]

        return res


if __name__ == '__main__':
    solution = Solution()
    assert solution.numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert solution.numberOfArithmeticSlices([1, 3, 5, 7, 9]) == 6
