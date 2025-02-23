# Problem: Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(1, col):
                matrix[i][j] += matrix[i][j-1]
        for i in range(1, row):
            for j in range(col):
                matrix[i][j] += matrix[i-1][j]
        count = 0
 
        for pt1 in range(row):
            for pt2 in range(col):
                if matrix[pt1][pt2] == target:
                    count += 1
                for c in range(pt2):
                    if matrix[pt1][pt2] - matrix[pt1][c] == target:
                        count += 1

                for r in range(pt1):
                    if matrix[pt1][pt2] - matrix[r][pt2] == target:
                        count += 1

    
                for r in range(pt1):
                    for c in range(pt2):
                        if matrix[pt1][pt2] - matrix[r][pt2] - matrix[pt1][c] + matrix[r][c] == target:
                            count += 1
        return count
