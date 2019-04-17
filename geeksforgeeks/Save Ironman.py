#! /usr/bin/env python
# coding: utf-8

'''
题目：回文字符串 https://practice.geeksforgeeks.org/problems/save-ironman/0
主题：arrays & strings
公司：amazon & google

解题思路：
先把数字字母找出来，然后从前面往中间遍历，只要不是一样，直接打印no
'''

if __name__ == "__main__":
    count = int(input())

    for _ in range(count):
        s = input()
        flag = True
        s = ''.join([c for c in s if 'a' <= c and c <=
                     'z' or 'A' <= c and c <= 'Z' or '0' <= c <= '9'])
        l = len(s)

        for i in range(int(l/2)):
            if abs(ord(s[i]) - ord(s[l - 1 - i])) not in (0, 32):
                print('NO')
                flag = False
                break
        if flag:
            print('YES')

        sum()
