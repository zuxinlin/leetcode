#! /usr/bin/env python
# coding: utf-8


def find(data_dict, u):
    '''
    查
    '''

    while data_dict[u] != u:
        u = data_dict[u]  # 一直传递下去，只要 data_dict[u] != u

    return u


def union(data_dict, u, v):
    '''
    并
    '''

    u = find(data_dict, u)
    v = find(data_dict, v)
    data_dict[u] = v

def main():
    pass

if __name__ == '__main__':
    main()
