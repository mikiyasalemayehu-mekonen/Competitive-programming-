# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = set()
        i = 0
        j = 0
        sums= 0 
        while i<len(mat) and j<len(mat[0]):
            sums = sums + mat[i][j]
            visited.add((i,j)) 
            i = i + 1
            j = j + 1
            
        i = len(mat)-1
        j = 0
 
        while i>=0 and j<len(mat[0]):
            if (i,j) not in visited:
                sums = sums + mat[i][j]
                visited.add((i,j)) 
            i = i - 1
            j = j + 1
           
        return sums 
        