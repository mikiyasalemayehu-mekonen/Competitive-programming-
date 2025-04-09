# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        islands = 0
        def checker(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        def dfs(row,col):
            if grid[row][col]=="0":
                return
            grid[row][col]= "0"
            for up,down in dir:
                new_row = row + up
                new_col = col + down
                if checker(new_row,new_col):
                    dfs(new_row,new_col)
            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    islands = islands + 1
                    dfs(i,j)

        return islands


