#! /usr/bin/env python
# coding: utf-8

import collections


def consecutive(num):
    # count = 0

    # for i in xrange(num / 2 + 1, 0, -1):
    #     s = i

    #     for j in xrange(i - 1, 0, -1):
    #         if s + j < num:
    #             s += j
    #         elif s + j == num:
    #             count += 1
    #         else:
    #             break

    # return count

    # start, end = 1, 1
    # sum = 1
    # count = 0

    # while start <= num / 2:
    #     if sum < num:
    #         end += 1
    #         sum += end
    #     elif sum > num:
    #         sum -= start
    #         start += 1
    #     else:
    #         sum -= start
    #         start += 1
    #         count += 1

    # return count

    count = 0
    index = 1

    while index * (index + 1) < 2 * num:
        target = (1.0 * num - (index * (index + 1)) / 2) / (index + 1)

        if target - int(target) == 0.0:
            count += 1

        index += 1
        
    return count


def main():
    print consecutive(15)
    # assert consecutive(15) == 3
    # assert degreeOfArray(10) == 1


if __name__ == '__main__':
    main()