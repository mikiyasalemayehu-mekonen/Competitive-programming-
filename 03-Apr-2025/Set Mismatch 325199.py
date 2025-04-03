# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        n = len(nums)
        while i<n:
            correct_pos = nums[i] - 1
            if correct_pos!=i and  nums[correct_pos]!=nums[i]:
                nums[i],nums[correct_pos] = nums[correct_pos],nums[i]
            else:
                i = i + 1
        for i in range(n):
            correct_pos = nums[i] - 1
            if correct_pos!=i:
                return [nums[i],i+1]
