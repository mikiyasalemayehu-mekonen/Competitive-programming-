# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        tem  = {}
        res = 0
        n = len(answers)
        for ans in answers:
            if ans==0:
                res = res + 1
            else:
                if ans in tem:
                    if tem[ans] ==ans + 1:
                        tem[ans] = 1
                        res = res + ans + 1
                    else:
                        tem[ans] = tem[ans] + 1
                    
                else:
                    tem[ans] = 1
                    res = res + ans + 1 
        return res
        