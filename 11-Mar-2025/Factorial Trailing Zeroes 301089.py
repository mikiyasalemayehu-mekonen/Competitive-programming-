# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def factorial(n):
        if n==1 or n==0:
            return n
        return n*self.factorial(n-1)
    def trailingZeroes(self, n: int) -> int:
        product = factorial(n)
        count = 0
        while product%10==0: 
            count =  count + 1 
            product = product //10
        return count
        
        