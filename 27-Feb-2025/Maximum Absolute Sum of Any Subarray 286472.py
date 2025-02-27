# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float("-inf")
        min_sum = float("inf")
        for i in range(len(nums)):
            curr_sum = curr_sum + nums[i]
            max_sum = max(max_sum,curr_sum)
            if curr_sum<0:
                curr_sum = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = curr_sum + nums[i]
            min_sum = min(min_sum,curr_sum)
            if curr_sum>0:
                curr_sum = 0
        
        return max(abs(max_sum), abs(min_sum))