#! /usr/bin/env python
# coding: utf-8
"""
树
"""


class Node(object):
    """节点"""

    def __init__(self, value=-1, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class Tree(object):
    """
    树
    """

    def __init__(self):
        self.root = Node()
        self.queue = []

    def create_tree(self, data):
        """
        根据传入的数组构造一棵树
        """

        self.root = Node(data[0])
        data = data[1:]
        self.queue.append(self.root)

        for (index, _) in enumerate(data[1::2]):
            current = self.queue.pop(0)

            if current.left_child is None:
                node = Node(data[index * 2])
                current.left_child = node
                self.queue.append(node)

            if current.right_child is None:
                node = Node(data[index * 2 + 1])
                current.right_child = node
                self.queue.append(node)

    def level(self, root):
        """
        层次遍历
        """

        queue = [root]

        while queue:
            current = queue.pop(0)
            print current.value, '->',

            if current.left_child:
                queue.append(current.left_child)

            if current.right_child:
                queue.append(current.right_child)

    def front(self, root):
        """
        前序遍历递归实现
        """

        if root is None:
            return

        print root.value, '->',
        self.front(root.left_child)
        self.front(root.right_child)

    def front_stack(self, root):
        """
        前序遍历非递归实现
        """

        if root is None:
            return

        stack = []
        node = root

        while node or stack:
            # 如果当前节点不空，一直访问左子树
            while node:
                print node.value, '->',
                stack.append(node)
                node = node.left_child

            # 当前节点左子树为空，弹出该节点，并且访问右子树
            node = stack.pop()
            node = node.right_child

    def middle(self, root):
        """
        中序遍历
        """

        if root is None:
            return

        self.middle(root.left_child)
        print root.value, '->',
        self.middle(root.right_child)

    def middle_stack(self, root):
        """
        中序遍历非递归实现
        """

        if root is None:
            return

        stack = []
        node = root

        while node or stack:
            # 如果当前节点不空，一直访问左子树
            while node:
                stack.append(node)
                node = node.left_child

            # 当前节点左子树为空，弹出该节点，并且访问右子树
            node = stack.pop()
            print node.value, '->',
            node = node.right_child

    def last(self, root):
        """
        后序遍历
        """

        if root is None:
            return

        self.last(root.left_child)
        self.last(root.right_child)
        print root.value, '->',


def main():
    """
    main函数
    """

    tree = Tree()
    tree.create_tree(range(1, 10))
    root = tree.root

    # 层次遍历
    print '层次遍历：'
    tree.level(root)
    print
    print

    # 前序遍历
    print '前序遍历递归：'
    tree.front(root)
    print
    print '前序遍历非递归：'
    tree.front_stack(root)
    print
    print

    # 中序遍历
    print '中序遍历递归：'
    tree.middle(root)
    print
    print '中序遍历非递归：'
    tree.middle_stack(root)
    print
    print

    tree.last(root)


if __name__ == '__main__':
    main()
