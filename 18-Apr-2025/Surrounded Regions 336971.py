# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        row, col = len(board), len(board[0])
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        visit = set()

        def check(r, c):
            return 0 <= r < row and 0 <= c < col

        def dfs(r, c):
            visit.add((r, c))
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if check(nr, nc) and board[nr][nc] == 'O' and (nr, nc) not in visit:
                    dfs(nr, nc)

        for i in range(row):
            for j in [0, col - 1]:
                if board[i][j] == 'O' and (i, j) not in visit:
                    dfs(i, j)

        for j in range(col):
            for i in [0, row - 1]:
                if board[i][j] == 'O' and (i, j) not in visit:
                    dfs(i, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i, j) not in visit:
                    board[i][j] = 'X'
