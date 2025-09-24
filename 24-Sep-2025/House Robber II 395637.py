# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def  check (houses):
            n = len(houses)
            memo = {}
            def dp(i):
                if i==0:
                    return houses[0] 
                if i==1:
                    return max(houses[0],houses[1])
                if i not in memo:
                    memo[i] = max(dp(i-1),dp(i-2)+houses[i])
                return  memo[i]
            return dp(n-1)
        tem1 = check(nums[1:])
        tem2 = check(nums[:-1])
        return max(tem1,tem2)