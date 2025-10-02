# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        memo = {}
        def dp(i,j):
            if i>=n1 or j>=n2:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i]==text2[j] :
                memo[(i,j)] = 1 + dp(i+1,j+1)
            else:
                memo[(i,j)] = max(dp(i + 1 , j),dp(i , j + 1))
            return memo[(i,j)] 

            
        return dp(0,0) 