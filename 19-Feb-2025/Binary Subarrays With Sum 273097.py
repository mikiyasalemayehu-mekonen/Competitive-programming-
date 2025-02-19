# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        for i in range(1,len(nums)):
            nums[i]  = nums[i] + nums[i-1]
        
        prefix = {0:1}
        subarray = 0 

        for i in range(len(nums)):
            if nums[i] - goal in prefix:
                subarray = subarray  + prefix[nums[i]-goal]
            prefix[nums[i]] = prefix.get(nums[i],0) + 1
        return subarray

            