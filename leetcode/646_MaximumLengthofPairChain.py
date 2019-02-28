# coding: utf-8

'''
You are given n pairs of numbers. In every pair, the first number is always smaller
than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed.
You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]

Note:
The number of given pairs will be in the range [1, 1000].
'''


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """

        # 先排序，然后再选择
        pairs = sorted(pairs, key=lambda x: x[1])
        pairs.sort(cmp=lambda x, y: x[1] - y[1])
        cur, res = float('-inf'), 0

        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]:
                cur, res = p[1], res + 1

        return res

        # pairs.sort(cmp=lambda x, y: x[1] - y[1])
        # l = len(pairs)
        # print pairs
        # dp = [1] * l
        # result = 1
        #
        # for i in xrange(1, l):
        #     for j in xrange(0, i):
        #         if pairs[i][0] > pairs[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #
        #     if result < dp[i]:
        #         result = dp[i]
        #
        # return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.findLongestChain([[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]]) == 4
