# LeetCode Problem Solution

## Problem type

### Basic

1. Math
1. Bit Manipulation
1. SortData Structure

### Data Structure

1. String
1. Array
1. Linked List
1. Hash Table
1. Stack
1. Heap
1. Tree

### Algorithm

1. Dynamic Programming(DP)
1. Depth-first Search(DFS)
1. Binary Search
1. Backtracking
    1. 基本思想：选优搜索法，走不通就退回重选，按照深度优先搜索的策略，从根节点出发，深度搜索解空间
    1. 步骤：
        * 确定解空间(子集树、排列树二选一)
        * 确定节点的扩展搜索规则
        * 深度优先方式搜索解空间，用剪枝法避免无效搜索
    1. 实例：0-1背包问题、旅行商问题、八皇后问题

1. Greedy


1. Divide and Conquer
    1. 基本思想：将一个问题，分解为多个子问题，递归的去解决子问题，最终合并为问题的解
    1. 适用情况：
        * 确定解空间(子集树、排列树二选一)
        * 利用适于搜索的方法组织解空间
        * 利用深度优先法搜索解空间
        * 利用剪枝函数避免移动到不可能产生解的子空间
    1. 实例：二分查找、快速排序、合并排序、大整数乘法、循环赛日程表、棋盘覆盖、找出伪币、求最值