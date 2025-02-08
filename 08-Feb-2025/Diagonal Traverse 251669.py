# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)

        row = len(mat)
        col = len(mat[0])

        # for _ in range(n + m):
        x, y = 0, 0
        while True:
            key = x + y
            i, j = x, y

            while i >= 0 and j < col:
                diagonal[key].append(mat[i][j])
                i -= 1
                j += 1
            if key % 2 != 0:
                diagonal[key].reverse()
            # update the start pos
            if x != row - 1:
                x += 1
            else:
                y += 1

            if y == col:
                break
        res = []
        for val in diagonal.values():
            res.extend(val)

        return res