# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        left=0
        right=1
        print(nums)
        while left<right and right<len(nums):
            if nums[left]==0 and nums[right]==0:
                right+=1
            elif nums[left]==0 and nums[right]!=0:
                nums[left],nums[right] = nums[right], nums[left]
                left+=1
                right+=1
            else:  
                left+=1
                right+=1
        return nums
        