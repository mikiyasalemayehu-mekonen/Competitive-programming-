# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = [(0, -1, -1)]
        result = 0

        for i, num in enumerate(arr):
            while num <= stack[-1][1]:
                stack.pop()

            new_sum = (num * (i - stack[-1][2]) + stack[-1][0]) % MOD
            result = (result + new_sum) % MOD
            stack.append((new_sum, num, i)) 

        return result
      

