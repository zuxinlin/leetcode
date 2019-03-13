#! /usr/bin/env python
# coding: utf-8

'''
汉诺塔问题

'''

cache = {}


def hanoi(n, A, B, C):
    '''
    打印n层汉诺塔从最左边移动到最右边的全部过程
    '''

    if n == 1:
        print '%s -> %s' % (A, C)
    else:
        hanoi(n - 1, A, C, B) # 先把 n - 1 个塔从A经过C移到B
        hanoi(1, A, B, C) # 再把最后一个从A移到C
        hanoi(n - 1, B, A, C) # 最后再把 n - 1 个塔从B经过A移到C


def main():
    '''
    主函数
    '''

    print hanoi(10, 'A', 'B', 'C')


if __name__ == '__main__':
    main()
