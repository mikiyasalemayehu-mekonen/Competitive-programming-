# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        before = 0
        temp = []
        for c in bank:
            count = Counter(c)
            temp.append(count["1"])
        res = 1
        last = 0
        for i in range(len(temp)):
            if temp[i]!=0:
                res += last * temp[i]
                last = temp[i]
        
        return res-1
        



            