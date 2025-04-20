# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        
        return True
        
