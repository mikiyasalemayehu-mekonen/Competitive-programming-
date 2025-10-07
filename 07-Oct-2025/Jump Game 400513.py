# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n =len(nums)
        dp = {i:False for i in range(n)}
        dp[n-1] = True
        for i in range(n-2,-1,-1):
            max_jump_to_from_i = min(i + nums[i], n - 1)
            for k in range(i + 1, max_jump_to_from_i + 1):
                if dp[k]:
                    dp[i] = True
                    break
        return dp[0]
