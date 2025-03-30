# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()  
        left, right = 0, len(nums) - 1
        MOD = 10**9 + 7
        ans = 0
        
        pow2 = [1] * (len(nums))
        for i in range(1, len(nums)):
            pow2[i] = (pow2[i - 1] * 2) % MOD  

        while left<=right:
            if nums[left] + nums[right]>target:
                right = right - 1
            else:
                ans = ans + pow2[right-left]
                left = left + 1

        return ans % MOD

