# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0  

        for ptr2 in range(len(nums)):
            if nums[ptr2] != 0:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1] 
                ptr1 += 1  

         
                
        