"""
Problem: https://leetcode.com/problems/implement-trie-prefix-tree/
Idea:
Time: O(K) where K is word length
Space: O(N * K) where N: number of words, K: word length
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
param_2 = trie.search("apple")
param_2 = trie.search("app")
param_2 = trie.startsWith("app")
trie.insert("app")
param_2 = trie.search("app")
# param_3 = trie.startsWith(prefix)