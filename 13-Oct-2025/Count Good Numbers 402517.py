# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 1:
            return 5
        elif n % 2 == 0:
            t = n // 2
            tem1 = pow(5, t, MOD)
            tem2 = pow(4, t, MOD)
            ans = (tem1 * tem2) % MOD
            return ans
        else:
            t = n // 2
            tem1 = pow(5, t + 1, MOD)
            tem2 = pow(4, t, MOD)
            ans = (tem1 * tem2) % MOD
            return ans
        
        