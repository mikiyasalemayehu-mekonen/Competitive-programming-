# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n<=0:
            return False
        elif n%4==0:
            return self.isPowerOfFour(n//4)
        else:
            return False
        