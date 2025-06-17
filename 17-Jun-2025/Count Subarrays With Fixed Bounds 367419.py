# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_idx = -1
        max_idx = -1
        ivd_idx = -1
        res = 0
        for i in range(len(nums)):
            if nums[i]==minK:
                min_idx = i
            if nums[i]==maxK:
                max_idx = i
            if nums[i]<minK or nums[i]>maxK:
                ivd_idx = i
            res = res +  max(min(min_idx,max_idx)-ivd_idx,0)
        return res
            
