#! /usr/bin/env python
# coding: utf-8

import collections


def winner(andrea, maria, s):
    num = len(andrea)
    andrea_sum = 0
    maria_sum = 0

    for i in xrange(num):
        if s == 'Even' and i % 2 == 0:
            andrea_sum += andrea[i] - maria[i]
            maria_sum += maria[i] - andrea[i]

        if s == 'Odd' and i % 2 == 1:
            andrea_sum += andrea[i] - maria[i]
            maria_sum += maria[i] - andrea[i]

    if andrea_sum > maria_sum:
        return 'Andrea'
    elif andrea_sum == maria_sum:
        return 'Tie'
    else:
        return 'Maria'


def main():
    assert winner([1, 2, 3], [2, 1, 3], 'Even') == 'Maria'
    assert winner([1, 2, 3], [2, 1, 3], 'Odd') == 'Andrea'


if __name__ == '__main__':
    main()