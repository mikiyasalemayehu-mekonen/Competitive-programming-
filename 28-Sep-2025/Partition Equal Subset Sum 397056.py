# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: 
            return False
        target = total // 2
        memo = {}
        def fn(i,curr_sum):
            if curr_sum==total//2:
                return True
            if curr_sum>total//2 or i>=len(nums) :
                return False
            if (i,curr_sum) not in memo:
                memo[(i,curr_sum)] = fn(i+1,curr_sum + nums[i]) or fn(i+1,curr_sum)
            return memo[(i,curr_sum)]
        return fn(0,0)