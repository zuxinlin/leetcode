#! /usr/bin/env python
# coding: utf-8

'''
阶乘递归和非递归实现
0 1 2 6 24 ...
公式：f(n) = f(n - 1) * n
'''

# 缓存中间结果
cache = {}


def factorial(number):
    '''
    递归计算阶乘
    '''

    if number <= 1:
        cache[number] = number

        return number

    temp = number * cache[number - 1]
    cache[number] = temp

    return temp
    # return number * factorial(n - 1)


def factorial_new(number):
    '''
    非递归计算阶乘
    '''

    if number <= 1:
        return number

    result = 1

    for i in xrange(2, number + 1):
        result *= i

    return result


def main():
    '''
    主函数
    '''

    for i in xrange(10):
        print factorial(i),

    print "\n=============================="

    for i in xrange(10):
        print factorial_new(i),


if __name__ == '__main__':
    main()
