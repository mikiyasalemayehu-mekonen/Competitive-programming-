# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for w in dictionary:
            tem = trie
            for c in w:
                if c not in tem:
                    tem[c] = {}
                tem = tem[c]
            tem["#"] = True
        
        def check(w):
            tem = trie
            temp = []
            for c in w:
                if c not in tem:
                    return
                if c in tem:
                    temp.append(c)
                    tem = tem[c]
                if "#" in tem:
                    return "".join(temp)
            return w
            
            
        s = sentence.split(" ")

        for i, w in enumerate(s):
            t = check(w)
            if t:
                s[i] = t

        return " ".join(s)
        
