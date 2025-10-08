# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        tem = 0
        l = len(nums)
        k = 0
        res = 0
        while tem<n:
            if k<l and nums[k]<=tem+1:
                tem += nums[k]
                k = k + 1
            else:
                tem += tem + 1
                res = res + 1
        return res
