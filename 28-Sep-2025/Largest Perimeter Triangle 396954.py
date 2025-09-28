# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        for i in range(len(nums)-2):
         
            if nums[i] + nums[i + 1]>nums[i+2]:
                maxi = max(maxi, nums[i] +  nums[i + 1] + nums[i+2])
        return maxi
        