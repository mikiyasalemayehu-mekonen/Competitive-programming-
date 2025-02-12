# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0 or c==1:
            return True
        ptr1 = 0
        ptr2 = int(sqrt(c))
        print(ptr2)
        while ptr1<=ptr2:
            square_sum = pow(ptr1,2) +pow(ptr2,2)
            if square_sum == c:
                return True
            elif  square_sum > c:
                ptr2-=1
            else:
                ptr1+=1
        return False




        
        