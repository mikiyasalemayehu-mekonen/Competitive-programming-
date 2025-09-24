# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i,j):
            if i>m or j>n:
                return 0
            elif i==m or j==n:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            down = dp(i+1,j)
            right = dp(i,j+1)
            memo[(i,j)] =  down + right
            return  memo[(i,j)]
        return dp(1,1)
        