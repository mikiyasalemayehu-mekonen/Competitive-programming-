# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        is_prime  = [True for _  in range(n)]
        is_prime[0] = is_prime[1]=False
        res = n-2
        d = 2
        while d * d <= n:
            if is_prime[d]:
                j = d*d
                while j<n :
                    if is_prime[j]:
                        res = res - 1
                    is_prime[j] = False
                    j = j + d
                    

            d = d + 1
     
        return is_prime.count(True)
