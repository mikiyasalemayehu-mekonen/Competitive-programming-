# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n ==1:
            return True
        elif n<1 or n%3!=0:
            return False
        else:
            return self.isPowerOfThree(n//3)
        
        