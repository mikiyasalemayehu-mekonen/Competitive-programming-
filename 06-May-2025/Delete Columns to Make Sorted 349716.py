# Problem: Delete Columns to Make Sorted - https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for j in range(len(strs[0])):
           
            for i in range(len(strs)-1):

                if strs[i][j]>strs[i+1][j]:
                    ans = ans + 1
                    break
        return ans