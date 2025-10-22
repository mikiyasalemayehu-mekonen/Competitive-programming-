# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
                node["cnt"] = node.get("cnt",0) + 1
        
        
        res = []
        for word in words:
            node = trie
            temp = 0
            for c in word:

                node = node[c]
                temp += node["cnt"] 
            res.append(temp)
        return res
        

        