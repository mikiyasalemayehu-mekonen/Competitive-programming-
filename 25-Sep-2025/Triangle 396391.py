# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        n = len(triangle)
        def dp(i,j):
            if i>=n or j>=i+1:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            res1 = float("inf")

            for k in range(j,min(len(triangle[i]),j+1)+1):
                print(k)
                res1 = min(res1,dp(i+1,k))
            
          

            # down = dp(i + 1, j)
            # down_right = dp(i + 1, j + 1)
            
            memo[(i, j)] = triangle[i][j] + res1
            return memo[(i,j)]
                
        return dp(0,0)