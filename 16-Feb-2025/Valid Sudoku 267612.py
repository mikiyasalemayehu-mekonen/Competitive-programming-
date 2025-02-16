# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            count = Counter(board[i])
            for key ,value in count.items():
                if key!="." and value>1:
                    return False
     
                
        for i in range(9):
            count = {}
            for j in range(9):
                count[board[j][i]] = count.get(board[j][i],0) + 1
            for key ,value in count.items():
                if key!="." and value>1:
                    return False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                count = Counter()
                for i in range(3):
                    for j in range(3):
                        num = board[box_row + i][box_col + j]
                        if num != ".":
                            count[num] += 1
                            if count[num] > 1:
                                return False
        
        return True
            
        return True

        