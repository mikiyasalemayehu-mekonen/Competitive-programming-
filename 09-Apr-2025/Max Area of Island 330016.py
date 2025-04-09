# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        visited = set()
        dir = [(0,1),(1,0),(-1,0),(0,-1)] 

        def checker(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        def dfs(row,col,a):
            visited.add((row,col))
            if grid[row][col]==0:
                return 0
            area = 1
            for u,v in dir:
                new_row = row + u
                new_col = col + v
                if checker(new_row,new_col) and (new_row,new_col) not in visited:
                    area = area + dfs(new_row,new_col,area)
            return area
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]==1:
                    max_area = max(max_area,dfs(i,j,0))

        return max_area
