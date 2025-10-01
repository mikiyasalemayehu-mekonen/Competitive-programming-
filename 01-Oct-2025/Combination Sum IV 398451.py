# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        memo = { } 
        def dp(w):
            if w==0:
                return 1
            if w<0:
                return 0
            ans = 0
            if (w) in memo:
                return  memo[w]
            for num in nums:
                ans += dp(w-num) 
            memo[w] = ans
            return memo[w]
        return dp(target)
            
        