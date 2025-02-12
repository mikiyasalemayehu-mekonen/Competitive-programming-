# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        pts=[(0,0),(0,1),(1,1),(1,-1),(-1,1),(-1,-1),(0,-1),(1,0),(-1,0)]

        rows, cols = len(img), len(img[0])
        ans = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                total, count = 0, 0
                for dx, dy in pts:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        total += img[ni][nj]
                        count += 1
                ans[i][j] = total // count
        
        return ans
        