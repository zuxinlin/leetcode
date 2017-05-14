# coding: utf-8

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
