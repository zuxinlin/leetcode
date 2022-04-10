#!/bin/env python
# coding: utf-8

# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。 
# 
#  实现 MyHashSet 类： 
# 
#  
#  void add(key) 向哈希集合中插入值 key 。 
#  bool contains(key) 返回哈希集合中是否存在这个值 key 。 
#  void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。 
#  
#  
# 
#  示例： 
# 
#  
# 输入：
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove
# ", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# 输出：
# [null, null, null, true, false, null, true, null, false]
# 
# 解释：
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // 返回 True
# myHashSet.contains(3); // 返回 False ，（未找到）
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // 返回 True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // 返回 False ，（已移除） 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= key <= 106 
#  最多调用 104 次 add、remove 和 contains 。 
#  
# 
#  
# 
#  进阶：你可以不使用内建的哈希集合库解决此问题吗？ 
#  Related Topics 设计 哈希表 
#  👍 158 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hash_table = [None] * self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size

        if not self.hash_table[index]:
            # We do not have anything in this bin, just create a new node
            self.hash_table[index] = ListNode(key)
        else:
            # We do have something in this bin, traverse it checking to see if we have a matching key.
            # If not just append a node to the end of the bin
            curr_node = self.hash_table[index]

            while curr_node:
                if curr_node.key == key:
                    return
                if not curr_node.next:
                    break
                curr_node = curr_node.next
                # Did not find a matching key here, so append a key, value pair in this bin
            curr_node.next = ListNode(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size

        curr_node = prev_node = self.hash_table[index]

        # Removing from empty bin just return
        if not curr_node:
            return

        if curr_node.key == key:
            # We found the node to delete immediately, we can now skip over it
            self.hash_table[index] = curr_node.next
        else:
            # We did not find the node to delete we must now traverse the bin
            curr_node = curr_node.next

            while curr_node:
                if curr_node.key == key:
                    prev_node.next = curr_node.next
                    break
                else:
                    prev_node, curr_node = prev_node.next, curr_node.next

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = key % self.size
        curr_node = self.hash_table[index]

        while curr_node:
            if curr_node.key == key:
                return True
            else:
                curr_node = curr_node.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    pass
