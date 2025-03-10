# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        for answer in answers:
            count[answer] = count.get(answer,0)+1
        minimum=0
        for key,value in count.items():
            if key > value:
                minimum = minimum  + key + 1
            elif  key  == value:
                minimum = minimum  + key  + 1
            elif  key + 1  == value:
                minimum = minimum  + value
            else:
                minimum = minimum  + math.ceil(value/(key+1))*(key+1)
                

        return minimum 