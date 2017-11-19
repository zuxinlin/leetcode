# coding: utf-8

'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # 两个码字的对应比特取值不同的比特数称为这两个码字的海明距离
        # 计算方法：对两个位串进行异或（xor）运算，并计算出异或运算结果中1的个数
        # 算二进制中1的个数：与1做与运算，右移

        return bin(x ^ y).count('1')

if __name__ == '__main__':
    solution = Solution()
    assert solution.hammingDistance(1, 4) == 2