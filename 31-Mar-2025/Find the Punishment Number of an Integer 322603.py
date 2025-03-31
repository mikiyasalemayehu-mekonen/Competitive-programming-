# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        def backtrack(square_str, index, current_sum):
            if index == len(square_str):
                return current_sum == sqrt(int(square_str))
            for i in range(index, len(square_str)):
                num_part = int(square_str[index:i+1]) 
               
                if backtrack(square_str, i+1, current_sum + num_part):
                    return True
            return False

        for i in range(1, n+1):
            square = i * i
            if backtrack(str(square), 0, 0):  
                ans += square 
        
        return ans


        