#! /usr/bin/env python
# coding: utf-8

import Queue
import sys

'''
树
'''


class Node(object):
    '''节点'''

    def __init__(self, value=-1, left_child=None, right_child=None, parent=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent


class Tree(object):
    '''
    树
    '''

    def __init__(self):
        self.root = Node()
        self.queue = []

    def create_tree(self, data):
        '''
        根据传入的数组构造一棵树
        '''

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

    def level_traversal(self, root):
        '''
        BFS，层次遍历，队列实现
        '''

        queue = Queue.Queue()  # 创建先进先出队列
        queue.put(root)

        while not queue.empty():
            current = queue.get()  # 弹出第一个元素并打印
            print current.value, '->',

            if current.left_child:  # 若该节点存在左子节点,则加入队列（先push左节点）
                queue.put(current.left_child)

            if current.right_child:  # 若该节点存在右子节点,则加入队列（再push右节点）
                queue.put(current.right_child)

    def preorder_traversal(self, root):
        '''
        DFS，前序遍历递归实现
        '''

        if root is None:
            return

        print root.value, '->',
        self.preorder_traversal(root.left_child)
        self.preorder_traversal(root.right_child)

    def preorder_traversal_stack(self, root):
        '''
        DFS，前序遍历非递归实现
        '''

        if root is None:
            return

        current = root
        stack = [root]

        while stack:
            print current.value, '->',

            if current.right_child:
                stack.append(current.right_child)

            if current.left_child:
                stack.append(current.left_child)

            current = stack.pop()

    def inorder(self, root):
        '''
        DFS，中序遍历
        '''

        if root is None:
            return

        self.inorder(root.left_child)
        print root.value, '->',
        self.inorder(root.right_child)

    def inorder_stack(self, root):
        '''
        DFS，中序遍历非递归实现
        '''

        if root is None:
            return

        stack = []
        node = root

        while node or stack:
            while node:
                # 如果当前节点不空，一直访问左子树
                stack.append(node)
                node = node.left_child

            # 当前节点左子树为空，弹出该节点，并且访问右子树
            node = stack.pop()
            print node.value, '->',
            node = node.right_child

    def post_traversal(self, root):
        '''
        DFS，后序遍历
        '''

        if root is None:
            return

        self.post_traversal(root.left_child)
        self.post_traversal(root.right_child)
        print root.value, '->',

    def post_traversal_stack(self, root):
        '''
        DFS，后序遍历非递归
        使用两个栈结构
        第一个栈进栈顺序：左节点->右节点->根节点
        第一个栈弹出顺序：根节点->右节点->左节点(先序遍历栈弹出顺序：根->左->右)
        第二个栈存储为第一个栈的每个弹出依次进栈
        最后第二个栈依次出栈
        '''

        if root is None:
            return

        first_stack = [root]
        second_stack = []

        while first_stack:
            current = first_stack.pop()
            second_stack.append(current)

            if current.left_child:
                first_stack.append(current.left_child)

            if current.right_child:
                first_stack.append(current.right_child)

        while second_stack:
            current = second_stack.pop()
            print current.value, '->',

    def node_num(self, root):
        '''
        树节点个数
        '''

        if root is None:
            return 0

        left_num = self.node_num(root.left_child)
        right_num = self.node_num(root.right_child)

        return 1 + left_num + right_num

    def depth(self, root):
        '''
        树深度
        '''

        if root is None:
            return 0

        left_depth = self.depth(root.left_child)
        right_depth = self.depth(root.right_child)

        return max(left_depth, right_depth) + 1

    def is_balance_binary_tree(self, root):
        '''
        平衡二叉树是一棵二叉树，其可以为空，或满足如下性质：左右子树深度之差的绝对值不大于1。
        '''

        if root is None:
            return True

        left_depth = self.depth(root.left_child)
        right_depth = self.depth(root.right_child)

        if abs(left_depth - right_depth) > 1:
            return False

        return self.is_balance_binary_tree(root.left_child) and self.is_balance_binary_tree(root.right_child)

    def is_binary_search_tree(self, root):
        '''
        是否二叉搜索树（中序遍历，值依次增大）
        1. 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
        2. 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
        3. 任意节点的左、右子树也分别为二叉查找树；
        4. 没有键值相等的节点。
        '''

        if root is None:
            return False

        max_value = -1000
        stack = []
        node = root

        while node or stack:
            if node:
                stack.append(node)
                node = node.left_child
            else:
                node = stack.pop()

                if node.value > max_value:
                    return False
                else:
                    max_value = node.value

                node = node.left_child

        return True

    def is_complete_binary_tree(self, root):
        '''
        是否完全二叉树
        若设二叉树的深度为h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（除了最后一层之外的其他每一层都被完全填充，并且所有结点都保持向左对齐。）

        左无、右有 ==> 返回 False
        左无、右无 ==> 激活判断：之后所有节点都是叶节点
        左有、右无 ==> 激活判断：之后所有节点都是叶节点        ==》      只要右无之后都必须是叶节点
        左有、右有 ==> 不用处理
        '''

        if root is None:
            return False

        queue = Queue.Queue()
        queue.put(root)
        flag = False  # 是否激活判断过程

        while not queue.empty():
            current = queue.get()

            if current.left_child:
                queue.put(current.left_child)

            if current.right_child:
                queue.put(current.right_child)

            if current.left_child is None and current.right_child:
                return False

            if flag:  # 若过程激活则判断节点是否为叶节点
                if current.left_child or current.right_child:
                    return False

            if not (current.left_child and current.right_child):  # 左不空、右空 | 左空、右空
                flag = True

        return True


def main():
    '''
    main函数
    '''

    tree = Tree()
    tree.create_tree(range(1, 10))
    root = tree.root

    # 树节点个数和深度
    print '树节点个数：%s, 树深度：%s, 是否平衡二叉树：%s, 是否搜索二叉树：%s, 是否完全二叉树：%s' % (tree.node_num(root), tree.depth(
        root), tree.is_balance_binary_tree(root), tree.is_binary_search_tree(root), tree.is_complete_binary_tree(root))
    print
    print

    # 层次遍历
    print '层次遍历：'
    tree.level_traversal(root)
    print
    print

    # 前序遍历
    print '前序遍历递归：'
    tree.preorder_traversal(root)
    print
    print '前序遍历非递归：'
    tree.preorder_traversal_stack(root)
    print
    print

    # 中序遍历
    print '中序遍历递归：'
    tree.inorder(root)
    print
    print '中序遍历非递归：'
    tree.inorder_stack(root)
    print
    print

    # 后序遍历
    print '后序遍历递归：'
    tree.post_traversal(root)
    print
    print '后序遍历非递归：'
    tree.post_traversal_stack(root)


if __name__ == '__main__':
    main()
