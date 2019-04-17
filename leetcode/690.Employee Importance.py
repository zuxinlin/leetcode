#! /usr/bin/env python
# coding: utf-8


from Queue import Queue

'''
题目：员工重要性 https://leetcode-cn.com/problems/employee-importance/
主题：hash table & depth-first search & breadth-first search

解题思路：
1. 先用哈希表缓存员工信息，深度优先遍历
'''


class Solution(object):
    '''
    '''

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        employee_dict = {employee.id: employee for employee in employees}

        def dfs(id): return employee_dict[id].importance + sum(
            [dfs(sub_id) for sub_id in employee_dict[id].subordinates])

        def bfs(id):
            queue = Queue()
            queue.put(employee_dict[id])
            value = 0

            while not queue.empty():
                employee = queue.get()
                value += employee.importance

                for sub_id in employee.subordinates:
                    queue.put(employee_dict[sub_id])

        return dfs(id)


if __name__ == '__main__':
    solution = Solution()
