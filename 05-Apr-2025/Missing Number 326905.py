# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expected = n*(n+1)//2
        sums = sum(nums)
        return expected - sums
        