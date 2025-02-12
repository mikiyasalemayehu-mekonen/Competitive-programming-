# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(height)-1
        while left<right:
            area = (right-left)*min(height[left],height[right])
            maximum = max(maximum, area)
            if height[left]<height[right]:
                left+=1
            else:
                right = right - 1  
        return maximum

        