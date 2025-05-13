# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        z = 2**n
        res = []
        for i in range(z):
            te = []
            for k in range(len(nums)):
                t = 1<<k
                tem =i&t
                if tem!=0:
                    te.append(nums[k])
            res.append(te)
        return res


            
