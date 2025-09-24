# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp(i):
            if i>n:
                return 0
            if i==n:
                return 0
            if i not in memo:
                use = cost[i] + dp(i+1)
                skip = cost[i] + dp(i+2)
                memo[i] = min(use,skip)
            return memo[i]
            
            
            
        return min(dp(0),dp(1))