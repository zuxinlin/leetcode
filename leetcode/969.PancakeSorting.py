#! /usr/bin/env python
# coding: utf-8

"""
"""

from itertools import permutations


class Solution(object):
    '''
    Given an array A, we can perform a pancake flip(饼子翻转): We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

    Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

    Example 1:

    Input: [3,2,4,1]
    Output: [4,2,4,3]
    Explanation: 
    We perform 4 pancake flips, with k values 4, 2, 4, and 3.
    Starting state: A = [3, 2, 4, 1]
    After 1st flip (k=4): A = [1, 4, 2, 3]
    After 2nd flip (k=2): A = [4, 1, 2, 3]
    After 3rd flip (k=4): A = [3, 2, 1, 4]
    After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
    Example 2:

    Input: [1,2,3]
    Output: []
    Explanation: The input is already sorted, so there is no need to flip anything.
    Note that other answers, such as [3, 3], would also be accepted.


    Note:

    1 <= A.length <= 100
    A[i] is a permutation of [1, 2, ..., A.length]
    '''

    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        res = []

        for x in range(len(A), 1, -1):
            # 查找最大的元素，然后翻转两次，第一次是从头到最大元素，第二次是整个数组，这样最大元素就跑到最后一个
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]

        return res


if __name__ == '__main__':
    solution = Solution()
    print solution.pancakeSort([3, 2, 4, 1])
