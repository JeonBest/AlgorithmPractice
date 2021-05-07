# LeetCode
# 720. Longest Word in Dictionary

class Solution:

    class Node:
        def __init__(self, key, count=0):
            self.key = key
            self.child = {}

    class Trie:
        def __init__(self):
            self.head = Node(None)
        
        def insert(word):
            curNode = self.head

            for letter in word:
                if letter not in curNode.child:
                    curNode.child [letter] = Node(letter)
                curNode = curNode.child[letter]
            curNode.child['*'] = True
        
        def search(word):
            curNode = self.head

            for letter in word:
                if letter in curNode.child:
                    curNode = curNode.child[letter]
            if '*' in curNode.child:
                return True
            else:
                return False

    def longestWord(self, words: List[str]) -> str:
