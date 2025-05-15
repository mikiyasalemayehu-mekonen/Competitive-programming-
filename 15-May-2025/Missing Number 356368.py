# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tem = nums[0]^0
        for i in range(1,len(nums)):
            tem = (tem)^i^nums[i]
        tem = tem^len(nums)
        return tem