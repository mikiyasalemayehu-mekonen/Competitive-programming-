# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(row, mat, cols, diag1, diag2):
            if row == n:
                res.append([''.join(r) for r in mat])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                mat[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1, mat, cols, diag1, diag2)

                mat[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0, board, set(), set(), set())
        return res
