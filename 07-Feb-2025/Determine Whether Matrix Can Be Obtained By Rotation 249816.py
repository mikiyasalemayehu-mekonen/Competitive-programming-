# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if mat == target:
            return True
        for _ in range(3):
            temp = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    temp[i][j] = mat[j][i]
            for i,cell in enumerate(temp):
                cell.reverse()
                temp[i] = cell
            if temp == target:
                return True
            mat = temp
        return False
        