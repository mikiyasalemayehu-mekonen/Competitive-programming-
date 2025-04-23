# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i-1]
        suffix = [0]*n
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] + nums[i+1]
        for i in range(n):
            prefix[i] = abs(prefix[i]-suffix[i])
        
        return prefix


        