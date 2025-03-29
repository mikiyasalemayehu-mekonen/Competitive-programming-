# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[R-1][C-1]:
            return False
        t, b = 0, R - 1
        while t <= b:
            m = (t + b) // 2
            if target == matrix[m][0]:
                return True
            elif target > matrix[m][0]:
                t += 1
            else:
                b -= 1
        left, right= 0, C - 1
        while left <= right:
            m = (left + right) // 2
            if target == matrix[b][m]:
                return True
            elif target > matrix[b][m]:
                left += 1
            else:
                right -= 1
        return False