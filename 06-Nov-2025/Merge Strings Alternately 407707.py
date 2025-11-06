# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        res = ""
        while l<len(word1) and r<len(word2):
            res = res + word1[l]
            res = res + word2[r]
            l = l +1
            r = r + 1
        if l<len(word1):
            res += word1[l:] 
        if r<len(word2):
            res += word2[r:] 
        return res
