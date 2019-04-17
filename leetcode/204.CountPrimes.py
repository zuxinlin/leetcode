#! /usr/bin/env python
# coding: utf-8

'''
题目： 统计素数 https://leetcode-cn.com/problems/count-primes/
主题： hash table & math

解题思路：
1. 利用数组缓存是否素数
'''


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        no_prime = [False] * n
        count = 0

        for i in range(2, n):
            if not no_prime[i]:
                count += 1

                for j in range(i, n/i+1):
                    if i * j < n:
                        no_prime[i*j] = True
                    else:
                        break

        return count


if __name__ == '__main__':
    solution = Solution()
    print ord('0') - ord('P')