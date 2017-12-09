#! /usr/bin/env python
# coding: utf-8

def permutation(s, start, end):
    if start == end:
        print ' '.join(s)

    for i in xrange(start, end + 1):
        s[start], s[i] = s[i], s[start]
        permutation(s, start + 1, end)
        s[start], s[i] = s[i], s[start]

def main():
    s = list('ABC')
    permutation(s, 0, len(s) - 1)

if __name__ == '__main__':
    main()