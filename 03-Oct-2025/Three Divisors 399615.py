# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False

        tem = n//2
        div = 2
        for i in range(2,tem+1):
          
            if n%i==0:
                div = div + 1
            if div>3:
                return False
        print(div)
        if div==3:
            return True
        return False
        