# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row = len(board)
        col = len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                        (0, 1),(1, -1), (1, 0), (1, 1)]

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col

        def countMines(r, c):
            count = 0
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if inbound(nr, nc) and board[nr][nc] == 'M':
                    count += 1
            return count

        def bfs(r, c):
            visited = set()
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()
                mines = countMines(r, c)
                if mines > 0:
                    board[r][c] = str(mines)
                else:
                    board[r][c] = 'B'
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if inbound(nr, nc) and board[nr][nc] == 'E' and (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))

        cr, cc = click
        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
        else:
            bfs(cr, cc)

        return board
