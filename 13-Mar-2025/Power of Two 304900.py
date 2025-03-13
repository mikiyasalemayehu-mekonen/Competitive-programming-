# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==1:
            return True
        elif n<1 or n%2!=0:
            return False
        else:
            return self.isPowerOfTwo(n//2)
        
        