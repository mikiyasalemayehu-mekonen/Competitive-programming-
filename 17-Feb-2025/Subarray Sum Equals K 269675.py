# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for  i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]

        count = 0
        can_make = {0:1}
        for x in range(len(nums)):
            if nums[x]-k in can_make :
                count = count + can_make[nums[x]-k]
            can_make[nums[x]] = can_make.get(nums[x],0) + 1
        return count
            
        