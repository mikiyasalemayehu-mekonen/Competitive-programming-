# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        request_sum = [0]*len(nums)
        for start,end in requests:
            request_sum[start] =  request_sum[start] + 1
            if end+1<len(nums):
                request_sum[end+1] = request_sum[end+1] - 1
        
        for i in range(1,len(request_sum)):
            request_sum[i] = request_sum[i-1] + request_sum[i]
        
        request_sum.sort()
        sums = 0
        for i in range(len(nums)):
            sums = sums + nums[i] * request_sum[i]
        return sums%(pow(10,9)+7)