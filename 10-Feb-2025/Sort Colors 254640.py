# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0]*3
        for num in nums:
            count[num] = count[num]+1
        index = 0
        print(count)
        for i in range(len(nums)):
            while count[index] ==0:
                index = index+1
            nums[i] = index
            count[index] = count[index]-1
           
        return nums
        