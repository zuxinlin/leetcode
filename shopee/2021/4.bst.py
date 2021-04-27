# coding: utf-8

pre_orders = map(str, raw_input().split())
in_orders = sorted(pre_orders)


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_bst(pre_orders, in_orders):
    '''
    构建排序二叉树
    :param pre_orders:
    :param in_orders:
    :return:
    '''
    if not pre_orders:
        return

    val = pre_orders[0]
    root = TreeNode(val)
    index = in_orders.index(val)
    root.left = create_bst(pre_orders[1:index + 1], in_orders[:index])
    root.right = create_bst(pre_orders[index + 1:], in_orders[index + 1:])

    return root


def pre_order(root):
    '''
    前序遍历
    :param root:
    :return:
    '''
    if not root:
        return

    if not root.left and not root.right:
        result.append(str(root.val))

    pre_order(root.left)
    pre_order(root.right)


result = []
root = create_bst(pre_orders, in_orders)
pre_order(root)
print(' '.join(result))
