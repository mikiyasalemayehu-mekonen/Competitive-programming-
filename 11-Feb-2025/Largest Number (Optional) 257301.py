# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums,key= lambda item:(str(item)*10),reverse=True)
        nums =[str(num) for num in nums]
        if nums[0]=="0":
            return "0"
        return "".join(nums)
        