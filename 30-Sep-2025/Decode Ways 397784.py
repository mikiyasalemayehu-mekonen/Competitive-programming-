# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        maps = {1:"A",2:"B"}
        n = len(s)
        memo ={}
        def dp(i):
            if i ==n:
                return 1
            if i in memo:
                return memo[i]
            ans = 0
            for j in range(i+1,min(i+3,n+1)):
                if s[i]=="0":
                    break
                if int(s[i:j])<=26 and int(s[i:j])>0 :
                    ans += dp(j)
            memo[i] = ans
            return memo[i]

        return dp(0)