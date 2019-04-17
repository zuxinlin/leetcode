#! /usr/bin/env python
# coding: utf-8

'''
题目：画家分区问题 https://practice.geeksforgeeks.org/problems/the-painters-partition-problem/0
主题：binary search & divide and conquer & dynamic programming & searching
公司：google

解题思路：
先把数字字母找出来，然后从前面往中间遍历，只要不是一样，直接打印no
'''

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        data = map(lambda x: int(x), input().split())
        result = [[0] * n for _ in range(n)]
        j = n - 1
        
        for index, element in enumerate(data):
            result[index % n][j] = element
            
            if index % n == n - 1:
                j -= 1
                
        merge = [str(item) for sub_list in result for item in sub_list]
        print(' '.join(merge))