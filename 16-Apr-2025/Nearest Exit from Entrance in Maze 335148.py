# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        row = len(maze)
        column = len(maze[0])
        ans = [0]
        def check(r,c):
            if r<0 or r>=row or c<0 or c>=column:
                return False
            if  maze[r][c]=="+":
                return False
            return True
        def valid(r,c):
            if (r==0 or c==0 or r==row-1 or c==column-1) and maze[r][c]==".":
                return True
            return False

        def bfs():
            visited = set()
            queue = deque()
            queue.append((entrance[0],entrance[1]))
            visited.add((entrance[0],entrance[1]))
            steps = 0
            while queue:
                length = len(queue)
                for i in range(length):
                    r,c = queue.popleft()
                    for dx,dy in dir:
                        new_row = r + dx
                        new_col = c + dy 
                        if (new_row,new_col) not in visited and check(new_row,new_col):
                            visited.add((new_row,new_col))
                            queue.append((new_row,new_col))
                            if valid(new_row,new_col):
                                return steps + 1
                            
                steps = steps + 1
            return -1
        return bfs()




