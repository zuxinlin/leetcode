#! /usr/bin/env python
# coding: utf - 8
"""
x^y计算
"""

from random import randint


def pow_new(base, number):
    """
    计算x的y次方值
    """
    # 递归退出条件
    if number == 0:
        return 1

    # 换成中间结果
    temp = pow_new(base, number / 2)

    # 判断奇偶数
    if number % 2 == 0:
        return temp * temp
    else:
        return base * temp * temp


def main():
    """
    main执行函数
    """

    for _ in xrange(10):
        base = randint(1, 10)
        number = randint(1, 3)
        print base, number
        assert pow_new(base, number) == pow(base, number)


if __name__ == '__main__':
    main()
