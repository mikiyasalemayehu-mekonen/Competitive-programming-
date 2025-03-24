# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        low  = -1  
        upper = -1
        i = 0 
        while i<len(nums):
            if nums[i]==target:
                if low==-1:
                    low = i
                upper = i
            i = i + 1
        return [low,upper]
        