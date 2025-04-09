# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        result = 0
        def checker(i,j):
            return  0<=i<len(grid) and 0<=j<len(grid[0])
        def dfs(i, j):
            nonlocal result
            if not checker(i, j) or grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:
                return 0
            grid[i][j] = -1 
            perimeter = 0
            for dx, dy in dir:
                ni, nj = i + dx, j + dy
                perimeter += dfs(ni, nj)
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0
