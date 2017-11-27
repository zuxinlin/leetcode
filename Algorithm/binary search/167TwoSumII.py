# coding: utf-8

'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # 采用库函数查找
        # ab = collections.Counter([i + j for i in A for j in B])
        #
        # return sum([ab[-i-j] for i in C for j in D])

        # 对半拆开计算，采用字典存储一半的加数结果，然后查找
        d = {}
        result = 0

        for i in A:
            for j in B:
                temp = i + j
                d[temp] = 1 if temp not in d else d[temp] + 1

        for i in C:
            for j in D:
                temp = 0 - i - j

                if temp in d:
                    result += d[temp]

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
