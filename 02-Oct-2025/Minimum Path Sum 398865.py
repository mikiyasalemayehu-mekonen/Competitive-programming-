# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        m = len(grid)
        n = len(grid[0])
        def dp(i,j):
           
            if i>=m or j>=n:
                return float("inf")
            if i == m - 1 and j == n - 1:
                return grid[i][j]
          
            if (i,j) in memo:
                return memo[(i,j)]
            down = grid[i][j] + dp(i+1,j)
            right = grid[i][j] + dp(i,j+1)
            memo[(i,j)] =  min(down , right)
            return  memo[(i,j)]
        return dp(0,0)
            
        