# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _  in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node =  node.children[idx]
        node.is_end = True
 

        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return False
            node =  node.children[idx]
        if not node.is_end:
            return False

        return True
        

    def startsWith(self, prefix: str) -> bool:
        node =  self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return False
            node =  node.children[idx]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)