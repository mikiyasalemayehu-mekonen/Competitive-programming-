# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length =max(nums)+1 
        count = [0]* length
        for num in nums:
            count[num]+=1
        for i in range(len(nums)):
            nums[i] = sum(count[:nums[i]])

        return nums
        