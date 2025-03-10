# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==0:
                return 1
            if n < 0:
                x = 1 / x
                n = -n
            if n % 2 == 0:
                half = power(x, n // 2)
                return half * half
            else:
                return x * power(x, n - 1)
                
        
        return power(x,n)