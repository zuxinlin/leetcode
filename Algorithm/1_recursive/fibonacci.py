#! /usr/bin/env python
# coding: utf-8

'''
斐波那契数列
0 1 1 2 3 5 ...
公式：f(n) = f(n - 1) + f(n - 2)
'''

# 缓存中间结果
cache = {}


def fibonacci(number):
    '''
    递归计算斐波那契数
    '''

    if number <= 1:
        cache[number] = number

        return number

    temp = cache[number - 1] + cache[number - 2]
    cache[number] = temp

    return temp
    # return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_new(number):
    '''
    非递归计算斐波那契数
    '''

    if number <= 1:
        return number

    first, second = 0, 1

    for _ in xrange(1, number):
        first, second = second, first + second

    return second


def main():
    '''
    主函数
    '''

    for i in xrange(10):
        print fibonacci(i),

    print

    for i in xrange(10):
        print fibonacci_new(i),


if __name__ == '__main__':
    main()
