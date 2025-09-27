# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        st = set(stones)
        n = len(stones)
        memo = {}
        def dp(i,units):
            if i==n-1:
                return True
            if (i,units) in memo:
                return memo[(i,units)]
            ans = False
            for u in range(max(0,units-1),units+2):
                tem = stones[i] + u 
                for k in range(i+1,n):
                    if tem == stones[k]:
                        ans = ans or dp(k,u)
            memo[(i,units)] = ans
                    
            return memo[(i,units)]

        return dp(0,0)
        