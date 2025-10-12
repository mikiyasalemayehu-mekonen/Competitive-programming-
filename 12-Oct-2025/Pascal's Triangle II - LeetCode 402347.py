# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1,rowIndex+1):
            tem = [1]
            for j in range(1,i):
                tem.append(res[j-1]+res[j])
            tem.append(1)
            res = tem
            print(res)

        return res
        