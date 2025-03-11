# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        row = self.getRow(rowIndex-1)
        temp = [1]
        for i in range(1,len(row)):
            temp.append(row[i-1] +  row[i]) 
        temp.append(1)
        return temp