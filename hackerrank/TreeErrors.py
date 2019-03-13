#! /usr/bin/env python
# coding: utf-8

# in_str = raw_input()
in_str = '(A,B (B,D) (B,C) (C,A)'


def check_multi_root(nodes):
    return ''


def check_more_child(nodes):
    d = {}
    f = {}

    for node in nodes:
        parent, child = node.split(',')
        d[parent] = (d[parent] + 1) if d.has_key(parent) else 1
        f[child] = (f[child] + 1) if f.has_key(child) else 1

        if d[parent] > 2:
            return 'E3'

        if f[child] > 1:
            return 'E4'

    return ''


def print_tree(nodes):
    pass


try:
    if not in_str.startswith('(') or not in_str.endswith(')'):
        raise Exception()

    nodes = in_str.split()

    for node in nodes:
        if node.startswith('(') and node.startswith(')'):
            nodes.append(node.replace('(', '').replace(')', ''))
        else:
            raise Exception()

    original_size = len(nodes)
    nodes = list(set(nodes))
    final_size = len(nodes)

    if original_size != final_size:
        print 'E2'
    else:
        result = check_more_child(nodes)

        if result != '':
            print result

        result = check_multi_root(nodes)

        if result != '':
            print result

        print_tree(nodes)
except:
    print 'E1'

class TreeNode(object):
    def __init__(self, element, left, right):
        pass