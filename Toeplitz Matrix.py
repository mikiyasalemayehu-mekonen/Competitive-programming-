class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        temp=matrix[0]
        for i in range(0,len(matrix)-1):
            for j in range(0,len(temp)-1):
                if (i+1<len(matrix) and j+1<len(temp)) and matrix[i][j]==matrix[i+1][j+1]:
                    continue
                else:
                    return False
                continue

        return True
        
