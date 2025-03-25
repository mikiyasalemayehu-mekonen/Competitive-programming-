# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = -1
        if target in nums:
            left = bisect_left(nums,target)
            right = bisect_right(nums,target)-1
        return [left,right]
        