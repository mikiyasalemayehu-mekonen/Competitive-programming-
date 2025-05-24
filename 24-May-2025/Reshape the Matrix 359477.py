# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]
        queue = deque(temp)
        ans =[]
        for i in range(r):
            tem =[ ]
            for j in range(c):


                if queue:
                    tem.append(queue.popleft())
                else:
                    return mat
            ans.append(tem)

        if len(queue)!=0:
            return mat
    
        return ans