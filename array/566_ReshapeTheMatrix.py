# coding: utf-8

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return nums

        sourceRow = len(nums)
        sourceColumn = len(nums[0])

        if sourceRow * sourceColumn != r * c:
            return nums
        else:
            result = []

            for i in xrange(r):
                columList = []

                for j in xrange(c):
                    count = i * c + j
                    m = count / sourceColumn
                    n = count % sourceColumn
                    columList.append(nums[m][n])

                result.append(columList)

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 2], [3, 4]]
    print sum(nums, [])

    r = 1
    c = 4
    # nums = [[1, 2, 3, 4]]
    # r = 2
    # c = 2
    assert [[1, 2, 3, 4]] == solution.matrixReshape(nums, r, c)
