# coding: utf-8

'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1
according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert
it to the form of 0+2i.

Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert
it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b
will both belong to the range of [-100, 100]. And the output should be also in this form.
'''


class Solution(object):
    def complexNumberMultiplyByMath(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a1, a2 = a.split('+')
        b1, b2 = b.split('+')
        a2 = a2[:-1]
        b2 = b2[:-1]

        c1 = int(a1) * int(b1) - int(a2) * int(b2)
        c2 = int(a1) * int(b2) + int(a2) * int(b1)

        return '%s+%si' % (c1, c2)

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # 转换成数据公式计算
        j, k = map(int, a[:-1].split('+'))
        m, n = map(int, b[:-1].split('+'))

        return '{}+{}i'.format(j * m - n * k, j * n + m * k)


if __name__ == '__main__':
    solution = Solution()
    assert solution.complexNumberMultiply("1+1i", "1+1i") == "0+2i"
    assert solution.complexNumberMultiply("1+-1i", "1+-1i") == "0+-2i"
