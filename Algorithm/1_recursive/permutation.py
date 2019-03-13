#! /usr/bin/env python
# coding: utf-8

'''
全排列
'''

cache = {}


def permutation(arr, i):
    '''
    
    '''

    if i == len(arr):
        print ' '.join(map(lambda i:str(i), arr))
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i] # 依次与当前及之后的数交换
            permutation(arr, i + 1)         # 打印当前数之后的全排列
            arr[i], arr[j] = arr[j], arr[i] # 把交换了的数字交换回去

def main():
    '''
    主函数
    '''

    permutation([1, 2, 3], 0)


if __name__ == '__main__':
    main()
