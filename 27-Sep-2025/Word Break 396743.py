# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        def dp(i):
            if i>=n:
                return True
            if i in memo:
                return memo[i]
            ans = False
            for j in range(i+1,n+1):
                if s[i:j] in wordDict:
                    ans = ans or dp(j)
            memo[i] = ans
            return memo[i]
        return dp(0)
        