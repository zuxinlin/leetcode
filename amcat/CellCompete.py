#! /usr/bin/env python
# coding: utf-8

import collections


def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    n = len(states)
    temp = [state for state in states]

    while days > 0:
        days -= 1
        temp[0] = 0 ^ states[1]
        temp[n - 1] = 0 ^ states[n - 2]

        for i in range(1, n - 1):
            temp[i] = states[i - 1] ^ states[i + 1]

        states = [i for i in temp]

    return states


def main():
    assert cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1) == [0, 1, 0, 0, 1, 0, 1, 0]
    assert cellCompete([1, 1, 1, 0, 1, 1, 1, 1], 2) == [0, 0, 0, 0, 0, 1, 1, 0]


if __name__ == '__main__':
    main()
