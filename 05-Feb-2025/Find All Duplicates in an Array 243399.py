# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        twice=[]
        for i in range(len(nums)):
            if nums[i]-1==i:
                continue
            else:   
                while nums[i]!=nums[nums[i]-1]:
                    temp=nums[i]-1
                    nums[i],nums[temp] = nums[temp],nums[i]
        for i in range(len(nums)):
            if nums[i]-1!=i and not nums[i] in twice:
                twice.append(nums[i])
        return twice 
        