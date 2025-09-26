# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        res = []
        while num>0:
            if num%2==0: 
                res.append("0")
            else:
                res.append("1")
            num = num//2
        res.reverse()
        for i,n in enumerate(res):
            if n=="0":
                res[i] = "1"
            else:
                res[i] = "0"

       

        return int("".join(res),2)

        