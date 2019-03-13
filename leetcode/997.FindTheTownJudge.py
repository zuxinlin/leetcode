#! /usr/bin/env python
# coding: utf-8

'''
题目： 找出小镇法官
主题： graph

解题思路：
1. 两个字典存储
'''


class Solution(object):
    '''
    '''

    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """

        # 边界
        if N == 1 and trust == []:
            return 1

        # 统计路径
        start_dict = {}
        end_dict = {}

        # 输入存储到字段
        for (start, end) in trust:
            end_dict[end] = 1 + end_dict[end] if end in end_dict else 1
            start_dict[start] = 1 + \
                start_dict[start] if start in start_dict else 1

        # 1. 法官不信任任何人；2. 其他人都信任法官；3. 只有一个法官
        for person in range(1, N + 1):
            if person in end_dict and end_dict[person] == N - 1 and person not in start_dict:
                return person

        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.findJudge(N=2, trust=[[1, 2]]) == 2
    assert solution.findJudge(N=3, trust=[[1, 3], [2, 3]]) == 3
    assert solution.findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1
    assert solution.findJudge(N=3, trust=[[1, 2], [2, 3]]) == -1
