# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor =[ ]
        def backtrack(i,xors):
            tem = xors
            for i in range(i,len(nums)):
                xors =nums[i]^tem
                xor.append(xors)
                backtrack(i+1,xors)
        
        backtrack(0,0)
        return sum(xor)      