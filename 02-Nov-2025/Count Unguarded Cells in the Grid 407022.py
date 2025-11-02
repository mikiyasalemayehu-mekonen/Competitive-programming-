# Problem: Count Unguarded Cells in the Grid - https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def inbound(i,j):
            return 0<=i<m and 0<=j<n
        dir = [[0,1],[1,0],[-1,0],[0,-1]]
        guard_set = {(gx, gy) for gx, gy in guards}
        wall_set = {(wx, wy) for wx, wy in walls}
        guarded = set()

        res = n*m
        for gx,gy in guards:
            for dx,dy in dir:
                x, y = gx + dx, gy + dy
                while inbound(x, y) and (x, y) not in guard_set and (x, y) not in wall_set:
                    guarded.add((x, y))
                    x += dx
                    y += dy

          
        return res - len(guard_set) - len(wall_set) - len(guarded)

        