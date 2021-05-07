# LeetCode
# 720. Longest Word in Dictionary

class Node:
    def __init__(self, key, count=0):
        self.key = key
        self.child = {}
class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, word):
        curNode = self.head
        for letter in word:
            if letter not in curNode.child:
                curNode.child [letter] = Node(letter)
            curNode = curNode.child[letter]
        curNode.child['*'] = True
    
    def searchValid(self, word):
        curNode = self.head
        isValid = True
        for letter in word:
            if curNode != self.head and '*' not in curNode.child:
                isValid = False
            if letter in curNode.child:
                curNode = curNode.child[letter]
        if '*' in curNode.child and isValid:
            return True
        else:
            return False

class Solution:
    def longestWord(self, words: list[str]) -> str:
        wordTrie = Trie()
        for word in words:
            wordTrie.insert(word)
        
        validwords = ""
        for word in words:
            if wordTrie.searchValid(word):
                # same length => lexicographical order
                if (len(word) == len(validwords) and word < validwords) or len(word) > len(validwords):
                    validwords = word
        
        return validwords

sol = Solution()
words = ["a","banana","app","appl","ap","apply","apple"]
print(sol.longestWord(words))