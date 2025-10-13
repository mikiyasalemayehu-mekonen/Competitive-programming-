# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        common = {}
        mini = inf
        for w in strs:
            mini = min(mini,len(w))
            tem = common
            for c in w:
                if c not in tem:
                    tem[c] = {}
                tem = tem[c]
        res = []
        while common:

            if len(common)>1:
                break
            tem = list(common.keys())
            res.append(tem[0])
            common = common[tem[0]]
       
        return "".join(res)[:mini]  
                    

        