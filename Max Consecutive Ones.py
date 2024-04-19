class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        num_zeros=0
        max_width=0
        for right in range(len(nums)):
            if nums[right]==0:
                num_zeros+=1
            while num_zeros>k:
                if nums[left]==0:
                    num_zeros-=1
                left+=1
            max_width=max(max_width,right-left+1)
        return max_width
        
        
