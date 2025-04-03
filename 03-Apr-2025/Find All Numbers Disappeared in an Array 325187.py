# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
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
                ans.append(i+1)

        return ans

        
        