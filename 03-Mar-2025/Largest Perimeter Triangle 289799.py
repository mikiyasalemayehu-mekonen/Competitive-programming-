# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        for i in range(2,len(nums)):
            sums = nums[i-1]+ nums[i]
            if nums[i-2]<sums:
                return sums+nums[i-2]
        return 0