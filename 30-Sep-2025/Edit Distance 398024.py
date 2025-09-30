# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        memo ={}
        if n1==0:
            return n2
        def dp(i,j):
            if j == n2:
                return n1-i
            ans = float("inf")
            if i==n1:
                return n2 - j 

                
                # return abs(j-i+1)

            if (i,j) in memo:
                return memo[(i,j)] 
            
            if word1[i]==word2[j]:
                ans = min(ans,dp(i+1,j+1))
            else:
                ch1 = 1+dp(i,j+1)
                ch2 = 1+dp(i+1,j)
                ch3 = 1 + dp(i+1,j+1)
                ans = min(ch1 ,ch2 ,ch3 )
            memo[(i,j)] = ans
            return memo[(i,j)] 
        return dp(0,0)

        