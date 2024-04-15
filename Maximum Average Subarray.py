class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum=sum(nums[:k])
        max_average=maximum/k
        for i in range(k,len(nums)):
            maximum+=nums[i]
            maximum-=nums[i-k]
            max_average=max(max_average,maximum/k)
        return max_average
        
