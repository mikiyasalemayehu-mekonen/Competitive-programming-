# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        before = nums[-1]
        mini  = inf
        for i in range(n-2,-1,-1):
            if nums[i] <= before:
                before = nums[i]
                continue
            k   = (nums[i]+before-1)//before
            res += (k-1) 
            before = nums[i]//k
        return res

        