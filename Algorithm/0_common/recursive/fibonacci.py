#! /usr/bin/env python
# coding: utf-8
"""
阶乘递归和非递归实现
"""


def fibonacci(number):
    """
    递归计算斐波那契数
    """

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_new(number):
    """
    非递归计算斐波那契数
    """

    if number <= 1:
        return number

    first, second = 0, 1

    for _ in xrange(1, number):
        first, second = second, first + second

    return second


def main():
    """
    主函数
    """

    for i in xrange(10):
        print fibonacci(i),

    print

    for i in xrange(10):
        print fibonacci_new(i),


if __name__ == '__main__':
    main()
