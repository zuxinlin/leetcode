#! /usr/bin/env python
# coding: utf-8

import datetime


def third_latest(dates):
    date_list = list(set([datetime.datetime.strptime(str(d), '%d-%m-%Y') for d in dates]))
    date_list = sorted(date_list)
    print [i.strftime('%Y-%m-%d') for i in date_list]

    return date_list[-3].strftime('%Y-%m-%d')


def main():
    print third_latest([
        '05-02-2017',
        '05-01-2017',
        '05-04-2017',
        '05-04-2017',
        '05-09-2017',
    ])


if __name__ == '__main__':
    main()