# coding: utf-8

'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

American keyboard

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''

class Solution(object):
    def check(self, word):
        firstSet = set('qwertyuiop')
        secondSet = set('asdfghjkl')
        thirdSet = set('zxcvbnm')

        # 用子集的方式判断
        wordSet = set(word.lower())

        return wordSet.issubset(firstSet) \
               or wordSet.issubset(secondSet) \
               or wordSet.issubset(thirdSet)

        # status = True
        # word = word.lower()
        #
        # for i in word:
        #     if status:
        #         status = i in firstSet
        #
        # if not status:
        #     status = True
        #
        #     for i in word:
        #         if status:
        #             status = i in secondSet
        #
        # if not status:
        #     status = True
        #
        #     for i in word:
        #         if status:
        #             status = i in thirdSet
        #
        # return status

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        return filter(self.check, words)

if __name__ == '__main__':
    solution = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    assert ["Alaska", "Dad"] == solution.findWords(words)