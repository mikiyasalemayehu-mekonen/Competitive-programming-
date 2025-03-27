# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = 5001
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low + high)//2
            if nums[mid] < minimum:
                minimum = nums[mid]
                if nums[mid]>nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[mid]>nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return minimum
        