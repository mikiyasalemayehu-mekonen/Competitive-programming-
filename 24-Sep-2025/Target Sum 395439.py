# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo =  {}
        def dp(i,w):
            if i>=n and w==target:
                return 1
            elif  i>=n:
                return 0
            
            if (i,w) in memo:
                return memo[(i,w)]

            include =  dp(i+1,w + nums[i])
            exclude =  dp(i+1,w -nums[i])
            memo[(i,w)] = include + exclude 
            return  memo[(i,w)] 
        return dp(0,0)
        
        