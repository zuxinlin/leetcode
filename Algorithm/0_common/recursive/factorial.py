#! /usr/bin/env python
# coding: utf-8
"""
阶乘递归和非递归实现
"""

def factorial(number):
    """
    递归计算阶乘
    """

    if number <= 1:
        return number

    return number * factorial(number - 1)

def factorial_new(number):
    """
    非递归计算阶乘
    """

    if number <= 1:
        return number

    result = 1

    for i in xrange(2, number + 1):
        result *= i

    return result


def main():
    """
    主函数
    """

    for i in xrange(10):
        print factorial(i),

    print

    for i in xrange(10):
        print factorial_new(i),


if __name__ == '__main__':
    main()
