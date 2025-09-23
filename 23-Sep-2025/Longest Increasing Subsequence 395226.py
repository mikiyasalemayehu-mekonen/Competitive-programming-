# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums) 
        memo = {}
        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = 1
            for j in range(i+1,n):
                include = 0 
                if nums[i] < nums[j]:
                    include = 1 +  dp(j)
                    memo[i] = max(memo[i], include)
            print(memo[i])

            return memo[i]

        res = 0
        for i in range(n):
            res = max(res,dp(i))
        return res

        