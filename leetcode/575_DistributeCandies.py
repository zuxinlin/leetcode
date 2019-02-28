# coding: utf-8

'''
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.
Note:

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
'''
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        # 看看有多少种糖果，因为需要一人分一半，所以需要看糖果种类和糖果总数一半进行比较
        return min(len(set(candies)), len(candies) / 2)

        # size = len(candies)
        # candy_dict = {}
        # count = 0
        #
        # for candy in candies:
        #     if candy_dict.has_key(candy):
        #         continue
        #     else:
        #         count += 1
        #         candy_dict[candy] = True
        #
        #     if count == size / 2:
        #         break
        #
        # return count

if __name__ == '__main__':
    solution = Solution()
    candies = [1,1,2,2,3,3]
    assert 3 == solution.distributeCandies(candies)
    candies = [1,1,2,3]
    assert 2 == solution.distributeCandies(candies)
