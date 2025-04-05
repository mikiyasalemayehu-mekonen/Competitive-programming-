# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = 0 
        maximum_count = -1
        for i in range(len(mat)):
            count = Counter(mat[i]) 
            count_one = count.get(1,0)
            if count_one>maximum_count:
                ans = i
                maximum_count = count_one
        return [ans,maximum_count]
        