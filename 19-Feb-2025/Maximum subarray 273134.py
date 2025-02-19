# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi= nums[0]
        currsum=0
        for num in nums:
            if currsum<0:
                currsum=0
            currsum+=num
            maxi=max(currsum,maxi)

            
        return maxi


        
        
        