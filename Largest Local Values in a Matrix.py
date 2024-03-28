class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(grid)-2):
            temp = []
            for j in range(len(grid[0])-2):
                if i+2 < len(grid) and j+2< len(grid[0]):
                    local_max = grid[i][j]
                    for k in range(i, i+3):
                        for l in range(j, j+3):
                            if grid[k][l] > local_max:
                                local_max = grid[k][l]
                    temp.append(local_max)
            if len(temp) > 0:
                ans.append(temp)
        return ans
              


        
