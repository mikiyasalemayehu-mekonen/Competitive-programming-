# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def inbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        path = {
            1: [(0, 1), (0, -1)],  
            2: [(1, 0), (-1, 0)],  
            3: [(0, -1), (1, 0)],  
            4: [(0, 1), (1, 0)],   
            5: [(0, -1), (-1, 0)], 
            6: [(0, 1), (-1, 0)]   
        }
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        root = {(i, j): (i, j) for i in range(len(grid)) for j in range(len(grid[0]))}

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])  
            return root[x]

        def union(t1, t2):
            parent_t1 = find(t1)
            parent_t2 = find(t2)
            if parent_t1 != parent_t2:
                root[parent_t2] = parent_t1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for d in directions:
                    nr, nc = i + d[0], j + d[1]
                    if inbound(nr, nc) and (d in path[grid[i][j]] and (-d[0], -d[1]) in path[grid[nr][nc]]):
                        union((i, j), (nr, nc))

        return find((0, 0)) == find((len(grid) - 1, len(grid[0]) - 1))
