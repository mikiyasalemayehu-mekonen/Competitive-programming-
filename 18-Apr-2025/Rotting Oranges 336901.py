# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        dir = [(0,1), (1,0), (0,-1), (-1,0)]
        minutes = -1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in dir:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1
