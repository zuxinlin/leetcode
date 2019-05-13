#! /usr/bin/env python
# coding: utf-8

from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = defaultdict(TrieNode)  # Easy to insert new node.
        self.is_word = False  # True for the end of the trie.


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root

        for char in word:
            curr = curr.nodes[char]

        curr.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root

        for char in word:
            if char not in curr.nodes:
                return False

            curr = curr.nodes[char]

        return curr.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root

        for char in prefix:
            if char not in curr.nodes:
                return False

            curr = curr.nodes[char]

        return True
