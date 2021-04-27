#! /usr/bin/env python
# coding: utf-8

# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通队列的全部四种操作（push、top、pop 和 empty）。 
# 
#  实现 MyStack 类： 
# 
#  
#  void push(int x) 将元素 x 压入栈顶。 
#  int pop() 移除并返回栈顶元素。 
#  int top() 返回栈顶元素。 
#  boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。 
#  
# 
#  
# 
#  注意： 
# 
#  
#  你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。 
#  你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 2, 2, false]
# 
# 解释：
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // 返回 2
# myStack.pop(); // 返回 2
# myStack.empty(); // 返回 False
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= x <= 9 
#  最多调用100 次 push、pop、top 和 empty 
#  每次调用 pop 和 top 都保证栈不为空 
#  
# 
#  
# 
#  进阶：你能否实现每种操作的均摊时间复杂度为 O(1) 的栈？换句话说，执行 n 个操作的总时间复杂度 O(n) ，尽管其中某个操作可能需要比其他操作更长的
# 时间。你可以使用两个以上的队列。 
#  Related Topics 栈 设计 
#  👍 316 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 存储栈内元素
        self.q1 = collections.deque()
        # 辅助队列，用来保障栈顶元素
        self.q2 = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q1.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
