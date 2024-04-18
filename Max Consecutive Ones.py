class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        temp=[0]
        start=0
        longest=0
        for i in range(len(nums)):
            if nums[i]==0 and temp[0]<=k:
                longest=max(longest,i-start+1)    
                temp[0]+=1
            elif nums[i]==0 and temp[0]>=k:
                start+=1
                temp[0]-=1
        return longest
