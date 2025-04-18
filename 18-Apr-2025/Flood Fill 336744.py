# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        column = len(image[0])
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        start = image[sr][sc]
        def inbound(r,c):
            if 0<=r<row and 0<=c<column:
                return True
            return False
        
        def valid(r,c):
            nonlocal start
            if image[r][c]==start:
                return True
            return False

        def bfs(r,c):
            nonlocal color
            visited = set()
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            image[r][c] = color
            while queue:
                r,c = queue.popleft()
                for dx,dy in dir:
                    new_row = r + dx
                    new_col = c + dy
                    if inbound(new_row,new_col) and (new_row,new_col) not in visited:                
                        if valid(new_row,new_col):
                            visited.add((new_row,new_col))
                            image[new_row][new_col] = color
                            queue.append((new_row,new_col))
    
        bfs(sr,sc)
        return image
