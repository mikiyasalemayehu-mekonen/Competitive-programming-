# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(matrix) for i in range(len(matrix[0])) ]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans[j][i] = matrix[i][j]
            
        return ans

           


        
        