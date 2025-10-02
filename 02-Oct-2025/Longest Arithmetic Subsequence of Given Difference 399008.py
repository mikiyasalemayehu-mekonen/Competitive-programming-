# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # n = len(arr)
        # maxi = max(arr)
        # mini = min(arr)-difference-1

        dp = {}
       
        for num in arr:
           
            dp[num] = dp.get(num-difference,0) + 1

        return max(dp.values())
        