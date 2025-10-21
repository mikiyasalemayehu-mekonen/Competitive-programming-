# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()  
        trie ={}
        res = ""
        for word in words:
            node = trie
            is_valid = True
            i = 0
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
                if "#" not in node and i!=len(word)-1:
                    is_valid = False
                i = i + 1
            node["#"] = True
            if is_valid and len(res)<len(word):
                res = word
    
    

        return res