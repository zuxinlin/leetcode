#! /usr/bin/env python
# coding: utf-8

from Queue import Queue
import sys

'''
树
'''


class Node(object):
    '''节点'''

    def __init__(self, val=-1, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Tree(object):
    '''
    树
    '''

    def __init__(self):
        self.root = Node()

    def create_tree(self, data):
        '''
        根据传入的数组构造一棵树，利用队列进行层次遍历
        '''

        self.root = Node(data[0])
        data = data[1:]
        queue = Queue()
        queue.put(self.root)

        for (index, _) in enumerate(data[::2]):
            cur = queue.get()

            if cur.left is None and data[index * 2]:
                node = Node(data[index * 2])
                cur.left = node
                queue.put(node)

            if cur.right is None and data[index * 2 + 1]:
                node = Node(data[index * 2 + 1])
                cur.right = node
                queue.put(node)

    def level_traversal(self, root):
        '''
        BFS，层次遍历，队列实现
        '''

        queue = Queue()  # 创建先进先出队列
        queue.put(root)

        while not queue.empty():
            cur = queue.get()  # 弹出第一个元素并打印
            print cur.val, '->',

            if cur.left:  # 若该节点存在左子节点,则加入队列（先push左节点）
                queue.put(cur.left)

            if cur.right:  # 若该节点存在右子节点,则加入队列（再push右节点）
                queue.put(cur.right)

    def preorder_traversal(self, root):
        '''
        DFS，前序遍历递归实现
        '''

        if root:
            print root.val, '->',
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def preorder_traversal_stack(self, root):
        '''
        DFS，前序遍历非递归实现
        '''

        if root is None:
            return

        stack = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                print cur.val, '->',
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right

    def inorder_traversal(self, root):
        '''
        DFS，中序遍历递归实现，时间复杂度O(n)，空间复杂度O(logn)
        '''

        if root is None:
            return

        self.inorder_traversal(root.left)
        print root.val, '->',
        self.inorder_traversal(root.right)

    def inorder_traversal_stack(self, root):
        '''
        DFS，中序遍历非递归实现，时间复杂度O(n)，空间复杂度O(logn)
        '''

        if root is None:
            return

        stack = []
        node = root

        while node or stack:
            if node:
                # 如果当前节点不空，一直访问左子树
                stack.append(node)
                node = node.left
            else:
                # 当前节点左子树为空，弹出该节点，并且访问右子树
                node = stack.pop()
                print node.val, '->',
                node = node.right

    def inorder_traversal_morris(self, root):
        '''
        DFS，中序遍历morris，时间复杂度O(n)，空间复杂度O(1)
        '''

        if root is None:
            return

        cur = root
        pre = None

        while cur:
            if cur.left is None:
                print cur.val, '->',
                cur = cur.right
            else:
                pre = cur.left

                while pre.right and pre.right != cur:
                    pre = pre.right

                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    print cur.val, '->',
                    cur = cur.right


    def post_traversal(self, root):
        '''
        DFS，后序遍历
        '''

        if root is None:
            return

        self.post_traversal(root.left)
        self.post_traversal(root.right)
        print root.val, '->',

    def post_traversal_two_stack(self, root):
        '''
        DFS，后序遍历非递归
        使用两个栈结构
        第一个栈进栈顺序：左 -> 右 -> 根
        第一个栈弹出顺序：根 -> 右 -> 左 
        第二个栈存储为第一个栈的每个弹出依次进栈
        最后第二个栈依次出栈
        '''

        if root is None:
            return

        first_stack = [root]
        second_stack = []

        while first_stack:
            cur = first_stack.pop()
            second_stack.append(cur)

            if cur.left:
                first_stack.append(cur.left)

            if cur.right:
                first_stack.append(cur.right)

        while second_stack:
            cur = second_stack.pop()
            print cur.val, '->',

    def node_num(self, root):
        '''
        树节点个数
        '''

        # 边界条件
        if root is None:
            return 0

        return 1 + self.node_num(root.left) + self.node_num(root.right)

    def depth(self, root):
        '''
        树深度
        '''

        # 边界条件
        if root is None:
            return 0

        return max(self.depth(root.left), self.depth(root.right)) + 1

    def is_balance_binary_tree(self, root):
        '''
        平衡二叉树是一棵二叉树，其可以为空，或满足如下性质：左右子树深度之差的绝对值不大于1。
        '''

        if root is None:
            return True

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        if abs(left_depth - right_depth) > 1:
            return False

        return self.is_balance_binary_tree(root.left) and self.is_balance_binary_tree(root.right)

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

        max_val = -1000
        stack = []
        node = root

        while node or stack:
            while node:
                # 如果当前节点不空，一直访问左子树
                stack.append(node)
                node = node.left

            # 当前节点左子树为空，弹出该节点，并且访问右子树
            node = stack.pop()

            if node.val < max_val:
                return False
            else:
                max_val = node.val

            node = node.right

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

        queue = Queue()
        queue.put(root)
        flag = False  # 是否激活判断过程

        while not queue.empty():
            cur = queue.get()

            if cur.left:
                queue.put(cur.left)

            if cur.right:
                queue.put(cur.right)

            if cur.left is None and cur.right:
                return False

            if flag:  # 若过程激活则判断节点是否为叶节点
                if cur.left or cur.right:
                    return False

            if not (cur.left and cur.right):  # 左不空、右空 | 左空、右空
                flag = True

        return True

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        stack = []
        result = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            result.append(cur)
            cur = cur.right

        root = result[0]
        cur = root
        cur.left = None

        for node in result[1:]:
            cur.right = node
            cur.left = None
            cur = node

        return root


def main():
    '''
    main函数
    '''

    tree = Tree()
    tree.create_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
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
    tree.inorder_traversal(root)
    print
    print '中序遍历非递归：'
    tree.inorder_traversal_stack(root)
    print
    print '中序遍历morris：'
    tree.inorder_traversal_morris(root)
    print
    print

    # 后序遍历
    print '后序遍历递归：'
    tree.post_traversal(root)
    print
    print '后序遍历非递归：'
    tree.post_traversal_two_stack(root)


if __name__ == '__main__':
    main()
