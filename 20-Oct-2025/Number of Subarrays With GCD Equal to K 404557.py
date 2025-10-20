# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            temp = nums[i]
            for j in range(i, n):
                temp = gcd(temp, nums[j])
                if temp == k:
                    res += 1
                elif temp < k:  
                    break
        return res

        