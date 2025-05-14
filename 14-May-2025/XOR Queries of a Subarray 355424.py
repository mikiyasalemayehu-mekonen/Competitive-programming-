# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [arr[0]]
        tem = arr[0]
    
        for i in  range(1,len(arr)):
            tem = tem^arr[i]
            xor.append(tem)
        res = []
      
        for l,r in queries:
            if l>0:
                t = xor[r]^xor[l-1]
            else:
                t = xor[r] 
            res.append(t)
        return res